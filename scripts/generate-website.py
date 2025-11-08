#!/usr/bin/env python3
"""
Generate all website pages from JSON data:
- Homepage (index.md)
- Publications page (publications.md)
- Projects page (projects.md)
"""

import json
from datetime import datetime
from pathlib import Path


def load_json(filename):
    """Load JSON data from the data directory."""
    data_dir = Path(__file__).parent.parent / 'data'
    with open(data_dir / filename, 'r') as f:
        return json.load(f)


def format_date(date_str):
    """Format date from YYYY-MM to Month YYYY."""
    if date_str.lower() == 'present':
        return 'Present'
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m')
        return date_obj.strftime('%b %Y')
    except Exception:
        return date_str


def make_author_bold(authors, name_to_bold):
    """Make the specified author name bold."""
    # If authors is a list, convert to string
    if isinstance(authors, list):
        authors_str = ', '.join(authors)
    else:
        authors_str = authors
    
    # Handle different name formats
    name_variations = [
        name_to_bold,
        name_to_bold.replace(',', ''),
        ' '.join(reversed(name_to_bold.split(', '))),
    ]
    
    for variation in name_variations:
        if variation in authors_str:
            authors_str = authors_str.replace(variation, f"**{variation}**")
            break
    
    return authors_str


def generate_homepage():
    """Generate the homepage (index.md)."""
    research_data = load_json('research.json')
    publications_data = load_json('publications.json')
    employment_data = load_json('employment.json')
    
    # Get latest items
    latest_research = research_data[0] if research_data else None
    latest_publication = publications_data[0] if publications_data else None
    latest_position = employment_data[0] if employment_data else None
    
    content = """---
layout: default
---

# Welcome to David's Cubicle ☕

I'm Hanchen David Wang, a PhD student at Vanderbilt University working on **eXplainable AI** and **Healthcare applications**. This is my digital space where I share my research, projects, and thoughts.

---

## Quick Links

- [Download my CV](./Resume.pdf)
- [View my Publications](./publications.html)
- [Check out my Projects](./projects.html)
- [Learn more About Me](./about.html)

---

## Recent Highlights

"""
    
    # Add latest research
    if latest_research:
        start = format_date(latest_research.get('startDate', ''))
        end = format_date(latest_research.get('endDate', 'Present'))
        title = latest_research.get('title', '')
        description = latest_research.get('description', [''])[0] if latest_research.get('description') else ''
        
        content += f"""**Latest Research**  
{title} ({start} - {end})  
{description}

"""
    
    # Add recent publication
    if latest_publication:
        title = latest_publication.get('title', '')
        venue = latest_publication.get('venue', '')
        status = latest_publication.get('status', '')
        
        status_text = f" - {status}" if status else ""
        content += f"""**Recent Publication**  
{title}  
{venue}{status_text}

"""
    
    # Add current position
    if latest_position:
        start = format_date(latest_position.get('startDate', ''))
        end = format_date(latest_position.get('endDate', 'Present'))
        org = latest_position.get('organization', '')
        position_title = latest_position.get('title', '')
        highlights = latest_position.get('highlights', [])
        description = highlights[0] if highlights else ''
        
        content += f"""**Current Position**  
{position_title} @ {org} ({start} - {end})  
{description}

"""
    
    content += """---

<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="font-size: 16px; color: #495057; margin: 0;">
    <strong>Let's connect!</strong> Feel free to reach out for collaborations or discussions about AI and healthcare.
  </p>
</div>
"""
    
    return content


def generate_publications():
    """Generate the publications page."""
    publications_data = load_json('publications.json')
    personal_data = load_json('personal.json')
    
    # Get Google Scholar link from personal data
    google_scholar_url = personal_data.get('social', {}).get('google_scholar', 'https://scholar.google.com')
    
    content = """---
layout: default
title: Publications
---

# Publications

A comprehensive list of my research publications in artificial intelligence, machine learning, and healthcare applications.

---

"""
    
    for i, pub in enumerate(publications_data, 1):
        title = pub.get('title', '')
        authors = pub.get('authors', '')
        venue = pub.get('venue', '')
        date = pub.get('date', '')
        status = pub.get('status', '')
        doi = pub.get('doi', '')
        arxiv = pub.get('arxiv', '')
        
        # Bold the user's name in authors
        authors = make_author_bold(authors, 'Wang, Hanchen David')
        authors = make_author_bold(authors, 'Hanchen David Wang')
        
        # Format the entry with title first (larger font) then authors
        content += f"{i}. <span style='font-size: 1.1em;'>**{title}**</span>  \n"
        content += f"   {authors}  \n"
        
        if venue:
            content += f"   {venue}"
            if date:
                content += f", {date}"
            if status:
                content += f", {status}"
            content += ".  \n"
        
        # Add links if available
        links = []
        if doi:
            # Add https://doi.org/ prefix if not already present
            doi_url = doi if doi.startswith('http') else f"https://doi.org/{doi}"
            links.append(f"[DOI]({doi_url})")
        if arxiv:
            # Add https://arxiv.org/abs/ prefix if not already present
            arxiv_url = arxiv if arxiv.startswith('http') else f"https://arxiv.org/abs/{arxiv}"
            links.append(f"[arXiv]({arxiv_url})")
        
        if links:
            content += f"   {' | '.join(links)}  \n"
        
        content += "\n"
    
    content += """---

<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="color: #495057; margin: 0;">
    For the most up-to-date list, visit my <a href="{}" target="_blank" style="color: #212529; font-weight: 600;">Google Scholar profile</a>
  </p>
</div>
""".format(google_scholar_url)
    
    return content


def generate_projects():
    """Generate the projects page."""
    projects_data = load_json('projects.json')
    
    # Get the path to the projects folder
    docs_dir = Path(__file__).parent.parent / 'docs' / 'projects'
    
    content = """---
layout: default
title: Projects
---

# Projects

A collection of my software engineering and development projects, showcasing work across various technologies and domains.

---

"""
    
    for project in projects_data:
        title = project.get('title', '')
        date = project.get('date', '')
        description = project.get('description', '')
        technologies = ', '.join(project.get('technologies', []))
        links = project.get('links', [])
        
        # Check if a project page exists in the /projects folder
        # Convert title to filename format (e.g., "Database Management System" -> "database-management-system.md")
        # Or check if the link points to an existing file
        has_detail_page = False
        link_url = '#'
        
        if links:
            link_url = links[0].get('url', '#')
            # Extract filename from URL (e.g., "./projects/PhysiQ.html" -> "PhysiQ.md")
            if './projects/' in link_url:
                filename = link_url.replace('./projects/', '').replace('.html', '.md')
                project_file = docs_dir / filename
                has_detail_page = project_file.exists()
        
        # If detail page exists, make title clickable; otherwise, just show as text
        if has_detail_page:
            content += f"""## [{title}]({link_url})
**{date}**

{description}

**Technologies:** {technologies}

---

"""
        else:
            content += f"""## {title}
**{date}**

{description}

**Technologies:** {technologies}

---

"""
    
    content += """
<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="color: #495057; margin: 0;">
    More projects and code samples available on <a href="https://github.com/HCWDavid" target="_blank" style="color: #212529; font-weight: 600;">GitHub</a>
  </p>
</div>
"""
    
    return content


def main():
    """Generate all website pages."""
    docs_dir = Path(__file__).parent.parent / 'docs'
    docs_dir.mkdir(exist_ok=True)
    
    # Generate homepage
    homepage_content = generate_homepage()
    homepage_path = docs_dir / 'index.md'
    with open(homepage_path, 'w') as f:
        f.write(homepage_content)
    print(f"✅ Homepage generated: {homepage_path}")
    
    # Generate publications page
    publications_content = generate_publications()
    publications_path = docs_dir / 'publications.md'
    with open(publications_path, 'w') as f:
        f.write(publications_content)
    print(f"✅ Publications page generated: {publications_path}")
    
    # Generate projects page
    projects_content = generate_projects()
    projects_path = docs_dir / 'projects.md'
    with open(projects_path, 'w') as f:
        f.write(projects_content)
    print(f"✅ Projects page generated: {projects_path}")
    
    print("\n🎉 All website pages generated successfully!")


if __name__ == '__main__':
    main()
