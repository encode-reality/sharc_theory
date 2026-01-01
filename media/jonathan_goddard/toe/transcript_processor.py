"""
Transcript Processor for Jonathan Goddard Interview
Splits the transcript into sections based on timestamps and creates organized folder structure
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict
import json


def parse_timestamps(timestamp_file: str) -> List[Tuple[str, str, str]]:
    """
    Parse the timestamp file and return a list of (timestamp, title, sanitized_folder_name)

    Args:
        timestamp_file: Path to the timestamps markdown file

    Returns:
        List of tuples containing (timestamp, section_title, folder_name)
    """
    timestamps = []

    with open(timestamp_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        # Parse format: "HH:MM:SS - Title"
        match = re.match(r'(\d{2}:\d{2}:\d{2})\s*-\s*(.+)', line)
        if match:
            timestamp = match.group(1)
            title = match.group(2).strip()

            # Create sanitized folder name
            folder_name = re.sub(r'[^\w\s-]', '', title.lower())
            folder_name = re.sub(r'[-\s]+', '_', folder_name)

            timestamps.append((timestamp, title, folder_name))

    return timestamps


def timestamp_to_seconds(timestamp: str) -> int:
    """Convert HH:MM:SS to total seconds"""
    parts = timestamp.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds


def parse_line_timestamp(line: str) -> int:
    """Extract timestamp in seconds from a transcript line"""
    match = re.match(r'\s*(\d{2}):(\d{2}):(\d{2})\.\d+', line)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        return hours * 3600 + minutes * 60 + seconds
    return -1


def split_transcript(transcript_file: str, timestamps: List[Tuple[str, str, str]]) -> Dict[str, List[str]]:
    """
    Split the transcript into sections based on timestamps

    Args:
        transcript_file: Path to the transcript file
        timestamps: List of (timestamp, title, folder_name) tuples

    Returns:
        Dictionary mapping folder_name to list of transcript lines
    """
    sections = {folder_name: [] for _, _, folder_name in timestamps}

    # Read transcript
    with open(transcript_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Convert timestamps to seconds for comparison
    timestamp_seconds = [(timestamp_to_seconds(ts), title, folder)
                         for ts, title, folder in timestamps]

    # Add header to preserve context
    header = []
    for i, line in enumerate(lines):
        if i < 3:  # First few lines are header
            header.append(line)
        else:
            break

    current_section_idx = 0

    for line in lines:
        line_time = parse_line_timestamp(line)

        if line_time == -1:
            # Not a timestamped line, skip or add to current section
            if current_section_idx < len(timestamp_seconds):
                sections[timestamp_seconds[current_section_idx][2]].append(line)
            continue

        # Find which section this line belongs to
        for idx in range(len(timestamp_seconds) - 1, -1, -1):
            if line_time >= timestamp_seconds[idx][0]:
                current_section_idx = idx
                break

        if current_section_idx < len(timestamp_seconds):
            sections[timestamp_seconds[current_section_idx][2]].append(line)

    # Add headers to each section
    for folder_name in sections:
        sections[folder_name] = header + sections[folder_name]

    return sections


def create_folder_structure(base_path: str, timestamps: List[Tuple[str, str, str]],
                           sections: Dict[str, List[str]]) -> None:
    """
    Create organized folder structure with transcript sections

    Args:
        base_path: Base directory for the organized content
        timestamps: List of (timestamp, title, folder_name) tuples
        sections: Dictionary of sections with transcript content
    """
    # Create main organized folder
    organized_path = Path(base_path) / "organized_transcript"
    organized_path.mkdir(exist_ok=True)

    # Create section folders and save transcripts
    section_info = []

    for idx, (timestamp, title, folder_name) in enumerate(timestamps):
        section_num = f"{idx+1:02d}"
        section_folder = organized_path / f"{section_num}_{folder_name}"
        section_folder.mkdir(exist_ok=True)

        # Save section transcript
        transcript_path = section_folder / "transcript.md"
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n")
            f.write(f"## Timestamp: {timestamp}\n\n")
            f.writelines(sections[folder_name])

        # Create placeholder for summary
        summary_path = section_folder / "summary.md"
        if not summary_path.exists():
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(f"# Summary: {title}\n\n")
                f.write(f"*To be generated*\n\n")
                f.write(f"## Key Concepts\n\n")
                f.write(f"## Main Points\n\n")
                f.write(f"## Related Topics to Study\n\n")

        section_info.append({
            'number': section_num,
            'timestamp': timestamp,
            'title': title,
            'folder': folder_name,
            'line_count': len(sections[folder_name])
        })

    # Save section index
    index_path = organized_path / "section_index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(section_info, f, indent=2)

    # Create main README
    readme_path = organized_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Jonathan Goddard Interview - Organized Transcript\n\n")
        f.write("## Interview: Quantum Gravity & Wolfram Physics Project\n\n")
        f.write("### Sections\n\n")

        for info in section_info:
            f.write(f"{info['number']}. **[{info['title']}](./{info['number']}_{info['folder']}/)**\n")
            f.write(f"   - Timestamp: {info['timestamp']}\n")
            f.write(f"   - Lines: {info['line_count']}\n\n")

    return organized_path


def main():
    """Main processing function"""
    base_dir = Path(__file__).parent

    # File paths
    timestamp_file = base_dir / "toe_transcript_timestamps.md"
    transcript_file = base_dir / "toe_transcript.md"

    print("="*60)
    print("Jonathan Goddard Interview Transcript Processor")
    print("="*60)

    # Parse timestamps
    print("\n[1/3] Parsing timestamps...")
    timestamps = parse_timestamps(timestamp_file)
    print(f"   Found {len(timestamps)} sections")

    # Split transcript
    print("\n[2/3] Splitting transcript...")
    sections = split_transcript(transcript_file, timestamps)

    total_lines = sum(len(lines) for lines in sections.values())
    print(f"   Processed {total_lines} lines")

    # Create folder structure
    print("\n[3/3] Creating folder structure...")
    organized_path = create_folder_structure(base_dir, timestamps, sections)
    print(f"   Created organized structure at: {organized_path}")

    print("\n" + "="*60)
    print("Processing complete!")
    print("="*60)
    print(f"\nOrganized transcript saved to: {organized_path}")
    print("\nNext steps:")
    print("1. Review section_index.json for section overview")
    print("2. Generate detailed summaries for each section")
    print("3. Research key concepts and add study guidance")


if __name__ == "__main__":
    main()
