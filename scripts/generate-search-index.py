#!/usr/bin/env python3
"""
Generate search index from all markdown files in docs/
"""
import json
import re
from pathlib import Path


def clean_text(text):
    """Remove markdown formatting and extra whitespace"""
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove markdown links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown headers
    text = re.sub(r'#+\s+', '', text)
    # Remove bold/italic
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text


def extract_title(content):
    """Extract title from markdown content"""
    # Try to find first h1
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    # Try to find title in frontmatter
    match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    return None


def generate_search_index():
    """Generate search index from all markdown files"""
    docs_dir = Path(__file__).parent.parent / 'docs'
    search_data = []
    
    # Find all markdown files recursively, excluding search.md and special files
    exclude_files = {'search.md', 'VISITOR_MAP_SETUP.md', 'another-page.md'}
    
    for md_file in docs_dir.rglob('*.md'):
        # Skip excluded files
        if md_file.name in exclude_files:
            continue
        
        # Skip files in _site directory
        if '_site' in md_file.parts:
            continue
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️  Skipping {md_file.name}: {e}")
            continue
        
        # Remove frontmatter
        content = re.sub(r'^---[\s\S]+?---\s*', '', content)
        
        # Extract title
        title = extract_title(content)
        if not title:
            title = md_file.stem.replace('-', ' ').title()
        
        # Clean and extract content
        cleaned_content = clean_text(content)
        
        # Generate URL relative to docs folder
        relative_path = md_file.relative_to(docs_dir)
        url = f"./{str(relative_path).replace('.md', '.html')}"
        
        # Determine page type for better categorization
        page_type = "Page"
        if 'projects/' in str(relative_path):
            page_type = "Project"
        elif md_file.name == 'index.md':
            page_type = "Home"
        elif md_file.name in ['about.md', 'publications.md', 'service.md', 'projects.md']:
            page_type = md_file.stem.replace('-', ' ').title()
        
        search_data.append({
            'title': title,
            'url': url,
            'content': cleaned_content[:1000],  # Limit content length
            'type': page_type
        })
    
    # Sort by type and title
    search_data.sort(key=lambda x: (x['type'] != 'Home', x['type'], x['title']))
    
    return search_data


def update_search_page(search_data):
    """Update search.md with new search data"""
    docs_dir = Path(__file__).parent.parent / 'docs'
    search_file = docs_dir / 'search.md'
    
    with open(search_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create search data JSON and escape backslashes for regex
    search_json = json.dumps(search_data, indent=2)
    search_json = search_json.replace('\\', '\\\\')
    
    # Replace the searchData in the script
    pattern = r'const searchData = \{[\s\S]*?\};'
    replacement = 'const searchData = {\n  pages: ' + search_json + '\n};'
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(search_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated search index with {len(search_data)} pages")


def main():
    print("📇 Generating search index...")
    search_data = generate_search_index()
    update_search_page(search_data)
    print("✅ Search index generated successfully!")


if __name__ == '__main__':
    main()
