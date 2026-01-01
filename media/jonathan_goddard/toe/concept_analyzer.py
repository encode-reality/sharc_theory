"""
Concept Analyzer for Jonathan Goddard Interview
Extracts key concepts, generates summaries, and creates study guides
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import Counter


class ConceptAnalyzer:
    """Analyzes transcript sections to extract concepts and generate summaries"""

    # Key technical terms and concepts to track
    TECHNICAL_TERMS = {
        # Physics & Math
        'quantum', 'relativity', 'gravity', 'spacetime', 'manifold', 'topology',
        'differential', 'calculus', 'tensor', 'metric', 'curvature', 'geodesic',
        'lagrangian', 'hamiltonian', 'entropy', 'thermodynamics', 'energy',

        # Computational Theory
        'turing', 'computation', 'algorithm', 'recursive', 'computational',
        'irreducibility', 'complexity', 'automata', 'halting', 'decidable',

        # Category Theory
        'category', 'functor', 'morphism', 'natural transformation', 'adjoint',
        'monad', 'topos', 'sheaf', 'homology', 'cohomology',

        # Set Theory
        'set theory', 'zermelo', 'fraenkel', 'axiom', 'cardinal', 'ordinal',

        # Wolfram Physics
        'hypergraph', 'rewriting', 'wolfram', 'cellular automata', 'rule',
        'multiway', 'causal graph', 'branchial', 'rulial',

        # Constructor Theory
        'constructor', 'substrate', 'transformation', 'deutsch', 'marletto',
        'catalyst', 'impossible', 'possible',

        # Logic & Foundations
        'godel', 'church', 'lambda', 'logic', 'proof', 'theorem', 'axiom',
        'formal', 'metalogic', 'consistency', 'completeness',

        # Philosophy of Science
        'ontology', 'epistemology', 'realism', 'instrumentalism', 'emergence',
        'reductionism', 'holism', 'paradigm', 'falsification',

        # Stone Duality
        'stone', 'duality', 'boolean algebra', 'topology', 'lattice', 'order',

        # Other
        'consciousness', 'spirituality', 'peer review', 'publishing',
    }

    PERSON_NAMES = {
        'wolfram', 'einstein', 'newton', 'leibniz', 'turing', 'church', 'godel',
        'deutsch', 'marletto', 'descartes', 'galileo', 'lorentz', 'tegmark',
        'piskunov', 'archimedes', 'penrose', 'hawking', 'feynman',
    }

    def __init__(self, organized_path: Path):
        self.organized_path = organized_path
        self.section_index = self._load_section_index()

    def _load_section_index(self) -> List[Dict]:
        """Load the section index JSON"""
        index_path = self.organized_path / "section_index.json"
        with open(index_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def extract_key_concepts(self, text: str) -> Dict[str, List[str]]:
        """
        Extract key concepts from text

        Returns:
            Dictionary with categories of concepts found
        """
        text_lower = text.lower()

        concepts = {
            'technical_terms': [],
            'people': [],
            'theories': [],
            'questions': [],
        }

        # Extract technical terms
        for term in self.TECHNICAL_TERMS:
            if term in text_lower:
                # Get context around the term
                pattern = re.compile(r'.{0,100}\b' + re.escape(term) + r'\b.{0,100}', re.IGNORECASE)
                matches = pattern.findall(text)
                if matches:
                    concepts['technical_terms'].append(term)

        # Extract person names
        for name in self.PERSON_NAMES:
            if name in text_lower:
                concepts['people'].append(name.title())

        # Extract questions (lines ending with ?)
        questions = re.findall(r'([^.!?]*\?)', text)
        concepts['questions'] = [q.strip() for q in questions[:5]]  # Limit to first 5

        # Remove duplicates
        for key in concepts:
            if isinstance(concepts[key], list):
                concepts[key] = list(dict.fromkeys(concepts[key]))

        return concepts

    def extract_main_topics(self, text: str) -> List[str]:
        """
        Extract main topics discussed in the text using keyword frequency

        Returns:
            List of main topics
        """
        text_lower = text.lower()

        # Count frequency of technical terms
        term_freq = Counter()

        for term in self.TECHNICAL_TERMS:
            count = text_lower.count(term)
            if count > 2:  # Significant mentions
                term_freq[term] = count

        # Get top terms
        top_terms = [term for term, _ in term_freq.most_common(10)]

        return top_terms

    def create_section_summary(self, section_info: Dict) -> Dict:
        """
        Create a comprehensive summary for a section

        Args:
            section_info: Section metadata from index

        Returns:
            Dictionary with summary information
        """
        section_folder = self.organized_path / f"{section_info['number']}_{section_info['folder']}"
        transcript_path = section_folder / "transcript.md"

        # Read transcript
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read()

        # Extract concepts
        concepts = self.extract_key_concepts(transcript_text)
        main_topics = self.extract_main_topics(transcript_text)

        # Extract key quotes (lines with high information density)
        lines = transcript_text.split('\n')
        key_lines = []

        for line in lines:
            # Skip header and timestamp lines
            if line.startswith('#') or re.match(r'\d{2}:\d{2}:\d{2}', line):
                continue

            # Look for lines with technical terms
            if any(term in line.lower() for term in main_topics[:5]):
                if len(line) > 50 and len(line) < 300:
                    key_lines.append(line.strip())

        summary = {
            'section_number': section_info['number'],
            'title': section_info['title'],
            'timestamp': section_info['timestamp'],
            'folder': section_info['folder'],
            'line_count': section_info['line_count'],
            'concepts': concepts,
            'main_topics': main_topics,
            'key_quotes': key_lines[:5],  # Top 5 quotes
        }

        return summary

    def generate_study_guide(self, summary: Dict) -> str:
        """
        Generate a study guide based on the summary

        Args:
            summary: Section summary dictionary

        Returns:
            Markdown formatted study guide
        """
        guide = f"# Study Guide: {summary['title']}\n\n"
        guide += f"**Section {summary['section_number']} | Timestamp: {summary['timestamp']}**\n\n"

        guide += "## Overview\n\n"
        guide += f"This section discusses {', '.join(summary['main_topics'][:5])}.\n\n"

        # Prerequisites
        guide += "## Prerequisites\n\n"
        guide += "To fully understand this section, you should be familiar with:\n\n"

        # Generate prerequisites based on concepts
        prereqs = self._generate_prerequisites(summary['concepts'], summary['main_topics'])
        for prereq in prereqs:
            guide += f"- {prereq}\n"

        guide += "\n"

        # Key Concepts
        guide += "## Key Concepts Discussed\n\n"
        if summary['concepts']['technical_terms']:
            guide += "### Technical Terms\n\n"
            for term in summary['concepts']['technical_terms'][:10]:
                guide += f"- **{term.title()}**\n"
            guide += "\n"

        if summary['concepts']['people']:
            guide += "### Key Figures Mentioned\n\n"
            for person in summary['concepts']['people']:
                guide += f"- {person}\n"
            guide += "\n"

        # Study Topics
        guide += "## Topics to Study Further\n\n"
        study_topics = self._generate_study_topics(summary)
        for i, topic in enumerate(study_topics, 1):
            guide += f"{i}. **{topic['title']}**\n"
            guide += f"   - Why: {topic['why']}\n"
            guide += f"   - Resources: {topic['resources']}\n\n"

        # Questions for Reflection
        guide += "## Questions for Reflection\n\n"
        if summary['concepts']['questions']:
            guide += "Questions raised in this section:\n\n"
            for q in summary['concepts']['questions'][:5]:
                guide += f"- {q}\n"
            guide += "\n"

        guide += "Additional questions to consider:\n\n"
        reflection_questions = self._generate_reflection_questions(summary)
        for q in reflection_questions:
            guide += f"- {q}\n"

        guide += "\n"

        # Connections
        guide += "## Connections to Other Fields\n\n"
        connections = self._identify_connections(summary)
        for conn in connections:
            guide += f"- **{conn['field']}**: {conn['description']}\n"

        guide += "\n"

        # Next Steps
        guide += "## Recommended Next Steps\n\n"
        guide += "1. Review the key concepts listed above\n"
        guide += "2. Research any unfamiliar technical terms\n"
        guide += "3. Explore the recommended study topics\n"
        guide += "4. Consider the reflection questions\n"
        guide += "5. Make connections to your existing knowledge\n\n"

        return guide

    def _generate_prerequisites(self, concepts: Dict, main_topics: List[str]) -> List[str]:
        """Generate list of prerequisites based on concepts"""
        prereqs = []

        if any(term in main_topics for term in ['quantum', 'relativity', 'gravity']):
            prereqs.append("Basics of quantum mechanics and general relativity")

        if any(term in main_topics for term in ['category', 'functor', 'morphism']):
            prereqs.append("Introduction to category theory")

        if any(term in main_topics for term in ['turing', 'computation', 'algorithm']):
            prereqs.append("Fundamentals of computer science and computability theory")

        if any(term in main_topics for term in ['set theory', 'axiom']):
            prereqs.append("Mathematical logic and set theory foundations")

        if any(term in main_topics for term in ['differential', 'manifold', 'topology']):
            prereqs.append("Differential geometry and topology")

        if any(term in main_topics for term in ['entropy', 'thermodynamics']):
            prereqs.append("Statistical mechanics and thermodynamics")

        if not prereqs:
            prereqs.append("General physics and mathematics background")

        return prereqs

    def _generate_study_topics(self, summary: Dict) -> List[Dict]:
        """Generate list of topics to study further"""
        topics = []

        main_topics = summary['main_topics']

        # Map topics to study recommendations
        topic_map = {
            'hypergraph': {
                'title': 'Hypergraph Rewriting Systems',
                'why': 'Core formalism of the Wolfram Physics Project',
                'resources': 'Wolfram Physics Project technical documentation, graph theory textbooks'
            },
            'category': {
                'title': 'Category Theory Foundations',
                'why': 'Provides alternative foundation to set theory and connects to constructor theory',
                'resources': 'Mac Lane "Categories for the Working Mathematician", Awodey "Category Theory"'
            },
            'constructor': {
                'title': 'Constructor Theory',
                'why': 'New framework for physical laws based on possible/impossible transformations',
                'resources': 'Papers by David Deutsch and Chiara Marletto on constructor theory'
            },
            'computational': {
                'title': 'Computational Irreducibility',
                'why': 'Fundamental limit on prediction in complex systems',
                'resources': 'Wolfram "A New Kind of Science", papers on complexity theory'
            },
            'stone': {
                'title': 'Stone Duality',
                'why': 'Mathematical duality connecting topology and logic',
                'resources': 'Topology textbooks, categorical logic papers'
            },
            'entropy': {
                'title': 'Entropy and Statistical Mechanics',
                'why': 'Fundamental concept in thermodynamics with deep connections to information theory',
                'resources': 'Jaynes "Probability Theory: The Logic of Science", statistical mechanics texts'
            },
        }

        for topic_key, topic_info in topic_map.items():
            if topic_key in main_topics:
                topics.append(topic_info)

        # Add at least 3 topics
        if len(topics) < 3:
            topics.append({
                'title': 'Foundations of Physics',
                'why': 'Understanding the philosophical and mathematical underpinnings of physical theories',
                'resources': 'Philosophy of physics texts, foundations of quantum mechanics'
            })

        return topics[:5]  # Limit to 5

    def _generate_reflection_questions(self, summary: Dict) -> List[str]:
        """Generate reflection questions based on content"""
        questions = []

        main_topics = summary['main_topics']

        if 'ontology' in main_topics or 'epistemology' in main_topics:
            questions.append("What is the relationship between mathematical models and physical reality?")
            questions.append("How do our cognitive tools shape our understanding of fundamental physics?")

        if 'computational' in main_topics:
            questions.append("What are the limits of computational models in describing nature?")
            questions.append("Is the universe fundamentally computational, or is computation just a useful model?")

        if 'category' in main_topics or 'set theory' in main_topics:
            questions.append("How do different mathematical foundations affect our physical theories?")

        if 'entropy' in main_topics:
            questions.append("What is the relationship between entropy, information, and the arrow of time?")

        if not questions:
            questions.append("What are the key insights from this section?")
            questions.append("How does this connect to other areas of physics and mathematics?")

        return questions

    def _identify_connections(self, summary: Dict) -> List[Dict]:
        """Identify connections to other fields"""
        connections = []

        main_topics = summary['main_topics']

        if 'computational' in main_topics or 'turing' in main_topics:
            connections.append({
                'field': 'Computer Science',
                'description': 'Computational models and complexity theory'
            })

        if 'category' in main_topics:
            connections.append({
                'field': 'Pure Mathematics',
                'description': 'Categorical foundations and abstract algebra'
            })

        if 'consciousness' in main_topics:
            connections.append({
                'field': 'Philosophy of Mind',
                'description': 'Nature of consciousness and its relationship to physical processes'
            })

        if 'entropy' in main_topics:
            connections.append({
                'field': 'Information Theory',
                'description': 'Connections between thermodynamic and information-theoretic entropy'
            })

        if not connections:
            connections.append({
                'field': 'Theoretical Physics',
                'description': 'General connections to foundational physics'
            })

        return connections

    def process_all_sections(self):
        """Process all sections and generate summaries and study guides"""
        print("\n" + "="*60)
        print("Concept Analyzer - Processing All Sections")
        print("="*60 + "\n")

        all_summaries = []

        for section in self.section_index:
            print(f"Processing Section {section['number']}: {section['title']}...")

            # Create summary
            summary = self.create_section_summary(section)
            all_summaries.append(summary)

            # Generate study guide
            study_guide = self.generate_study_guide(summary)

            # Save study guide
            section_folder = self.organized_path / f"{section['number']}_{section['folder']}"
            guide_path = section_folder / "study_guide.md"

            with open(guide_path, 'w', encoding='utf-8') as f:
                f.write(study_guide)

            print(f"   [OK] Created study guide: {guide_path.name}")

            # Update summary file
            summary_path = section_folder / "summary.md"
            summary_content = self._generate_summary_content(summary)

            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary_content)

            print(f"   [OK] Updated summary: {summary_path.name}\n")

        # Save master summary
        self._save_master_summary(all_summaries)

        print("="*60)
        print("All sections processed successfully!")
        print("="*60)

    def _generate_summary_content(self, summary: Dict) -> str:
        """Generate summary content in markdown"""
        content = f"# Summary: {summary['title']}\n\n"
        content += f"**Section {summary['section_number']} | Timestamp: {summary['timestamp']}**\n\n"

        content += "## Main Topics\n\n"
        for topic in summary['main_topics'][:8]:
            content += f"- {topic.title()}\n"
        content += "\n"

        content += "## Key Concepts\n\n"

        if summary['concepts']['technical_terms']:
            content += "### Technical Terms\n"
            for term in summary['concepts']['technical_terms'][:15]:
                content += f"- {term.title()}\n"
            content += "\n"

        if summary['concepts']['people']:
            content += "### Key Figures\n"
            for person in summary['concepts']['people']:
                content += f"- {person}\n"
            content += "\n"

        if summary['key_quotes']:
            content += "## Notable Excerpts\n\n"
            for i, quote in enumerate(summary['key_quotes'], 1):
                # Clean up the quote
                clean_quote = quote.replace('→', '').strip()
                if clean_quote:
                    content += f"{i}. {clean_quote}\n\n"

        content += "## Related Topics to Study\n\n"
        content += "See the `study_guide.md` file in this section for detailed study recommendations.\n\n"

        return content

    def _save_master_summary(self, all_summaries: List[Dict]):
        """Save a master summary of all sections"""
        master_path = self.organized_path / "MASTER_SUMMARY.md"

        content = "# Jonathan Goddard Interview - Master Summary\n\n"
        content += "## Complete Concept Map\n\n"

        # Aggregate all concepts
        all_technical_terms = set()
        all_people = set()
        all_topics = []

        for summary in all_summaries:
            all_technical_terms.update(summary['concepts']['technical_terms'])
            all_people.update(summary['concepts']['people'])
            all_topics.extend(summary['main_topics'])

        # Count topic frequency
        topic_freq = Counter(all_topics)

        content += "### Most Discussed Topics\n\n"
        for topic, count in topic_freq.most_common(15):
            content += f"- **{topic.title()}** (mentioned {count} times)\n"
        content += "\n"

        content += "### All Technical Terms\n\n"
        for term in sorted(all_technical_terms):
            content += f"- {term.title()}\n"
        content += "\n"

        content += "### Key Figures Referenced\n\n"
        for person in sorted(all_people):
            content += f"- {person}\n"
        content += "\n"

        content += "## Section-by-Section Overview\n\n"

        for summary in all_summaries:
            content += f"### {summary['section_number']}. {summary['title']} ({summary['timestamp']})\n\n"
            content += f"**Main Topics**: {', '.join(summary['main_topics'][:5])}\n\n"
            content += f"**Key Concepts**: {len(summary['concepts']['technical_terms'])} technical terms\n\n"
            content += "---\n\n"

        with open(master_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\nMaster summary saved to: {master_path}")


def main():
    """Main function"""
    base_dir = Path(__file__).parent
    organized_path = base_dir / "organized_transcript"

    if not organized_path.exists():
        print("Error: Please run transcript_processor.py first to create the organized structure.")
        return

    analyzer = ConceptAnalyzer(organized_path)
    analyzer.process_all_sections()


if __name__ == "__main__":
    main()
