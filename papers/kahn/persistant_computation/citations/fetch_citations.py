#!/usr/bin/env python3
import re
import json
import os
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = os.path.dirname(__file__)
BIB_PATH = os.path.join(os.path.dirname(ROOT), 'references.bib')
OUT_DIR = ROOT
MANIFEST_JSON = os.path.join(OUT_DIR, 'manifest.json')
RESOLVED_MD = os.path.join(OUT_DIR, 'RESOLVED.md')

def parse_bib(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    entries = []
    for m in re.finditer(r'@\w+\{([^,]+),(.*?)\n\}', text, flags=re.S):
        key = m.group(1).strip()
        body = m.group(2)
        fields = dict((fm.group(1).lower(), fm.group(2).strip()) for fm in re.finditer(r'\n\s*([a-zA-Z]+)\s*=\s*\{([^}]*)\}', body))
        title = fields.get('title', '')
        author = fields.get('author', '')
        year = fields.get('year', '')
        entries.append({'key': key, 'title': title, 'author': author, 'year': year})
    return entries

def http_json(url, headers=None):
    req = Request(url, headers=headers or {"User-Agent": "citation-fetch/0.1"})
    with urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

def download(url, dest):
    try:
        req = Request(url, headers={"User-Agent": "citation-fetch/0.1"})
        with urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
        return True
    except Exception:
        return False

def crossref_lookup(title, author, year, rows=3):
    q = quote(' '.join(x for x in [title, author, year] if x))
    url = f"https://api.crossref.org/works?query.bibliographic={q}&rows={rows}"
    try:
        data = http_json(url)
    except Exception:
        return []
    items = data.get('message', {}).get('items', [])
    results = []
    for it in items:
        doi = it.get('DOI')
        url = it.get('URL')
        links = it.get('link', [])
        pdf_link = None
        for lk in links:
            if lk.get('content-type') == 'application/pdf' and lk.get('URL'):
                pdf_link = lk['URL']
                break
        results.append({'doi': doi, 'url': url, 'pdf': pdf_link, 'item': it})
    return results

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    entries = parse_bib(BIB_PATH)
    manifest = {}
    for e in entries:
        key = e['key']
        title = e['title']
        author = e['author']
        year = e['year']
        status = {'key': key, 'title': title, 'author': author, 'year': year,
                  'doi': None, 'url': None, 'pdf_url': None, 'pdf_path': None, 'retrieved': False}
        results = crossref_lookup(title, author, year)
        if results:
            best = results[0]
            status['doi'] = best.get('doi')
            status['url'] = best.get('url')
            status['pdf_url'] = best.get('pdf')
            if best.get('pdf'):
                dest = os.path.join(OUT_DIR, f"{key}.pdf")
                if download(best['pdf'], dest):
                    status['pdf_path'] = os.path.basename(dest)
                    status['retrieved'] = True
        manifest[key] = status

    with open(MANIFEST_JSON, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    # Write a human-friendly markdown summary
    lines = ["# Resolved Citations", "", "| Key | DOI | URL | PDF |", "|---|---|---|---|"]
    for k in sorted(manifest.keys()):
        st = manifest[k]
        doi = st['doi'] or ''
        url = st['url'] or ''
        pdf = st['pdf_path'] or (st['pdf_url'] or '')
        lines.append(f"| {k} | {doi} | {url} | {pdf} |")
    with open(RESOLVED_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    main()

