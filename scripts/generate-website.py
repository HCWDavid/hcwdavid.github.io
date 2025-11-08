#!/usr/bin/env python3
"""
Generate all website pages from JSON data:
- Homepage (index.md)
- Publications page (publications.md)
- Projects page (projects.md)
- Leadership & Service page (service.md)
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


def generate_service():
    """Generate the leadership and service page."""
    service_data = load_json('service.json')
    
    content = """---
layout: default
title: Leadership & Service
---

# Leadership & Service

My contributions to the academic community through mentoring, volunteering, and service activities.

---

"""
    
    for i, service in enumerate(service_data, 1):
        title = service.get('title', '')
        organization = service.get('organization', '')
        location = service.get('location', '')
        start = format_date(service.get('startDate', ''))
        end = format_date(service.get('endDate', ''))
        highlights = service.get('highlights', [])
        
        # Format date range
        date_range = f"{start} - {end}" if start != end else start
        
        content += f"""## {title}
**{organization}** | {location}
**{date_range}**

"""
        
        # Add highlights as bullet points
        if highlights:
            for highlight in highlights:
                content += f"- {highlight}\n"
            content += "\n"
        
        content += "---\n\n"
    
    content += """
<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="color: #495057; margin: 0;">
    Interested in collaboration or mentorship opportunities? <a href="./about.html" style="color: #212529; font-weight: 600;">Get in touch!</a>
  </p>
</div>
"""
    
    return content


def generate_about():
    """Generate the about page."""
    education_data = load_json('education.json')
    personal_data = load_json('personal.json')
    
    content = """---
layout: default
title: About Me
---

<div class="about-page">
  <div class="profile-header">
    <img src="./assets/portfolio.png" alt="Hanchen David Wang" class="profile-photo">
    <h1>Hanchen David Wang</h1>
    <p class="tagline">{{ site.description }}</p>
    
    <!-- Social Links -->
    <div class="social-links-large">
      <a href="https://www.linkedin.com/in/hanchendavidwang/" target="_blank" title="LinkedIn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
        </svg>
        <span>LinkedIn</span>
      </a>
      <a href="./Resume.pdf" target="_blank" title="Download CV">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
        </svg>
        <span>Download CV</span>
      </a>
      <a href="https://github.com/HCWDavid" target="_blank" title="GitHub">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        <span>GitHub</span>
      </a>
    </div>
  </div>

  <section class="bio">
    <h2>👋 About Me</h2>
    <p>Welcome! My name is David. I am currently a PhD student at <strong>Vanderbilt University</strong> working with Prof. <a href="https://meiyima.github.io" target="_blank">Meiyi Ma</a> on <strong>eXplainable AI in Healthcare</strong> and <strong>Deep Learning research</strong>.</p>
    
    <p>I am passionate about advancing the fields of eXplainable AI (XAI), healthcare, and machine learning. My work focuses on leveraging cutting-edge machine learning techniques to improve physical therapy, nursing simulations, and formal verification in AI.</p>
  </section>

  <section class="interests">
    <h2>🎯 Research Interests</h2>
    <p>My research spans across multiple areas of artificial intelligence and computer science, with a focus on making AI systems more explainable, reliable, and beneficial for healthcare applications.</p>
    <p><strong>Key Areas:</strong> Explainable AI (XAI), Healthcare AI, Machine Learning, Physical Therapy & Motion Analysis, Nursing Education Simulations, Formal Verification, Multimodal Learning, Continual Learning</p>
  </section>

  <section class="education">
    <h2>🎓 Education</h2>
"""
    
    # Generate education items from JSON
    for edu in education_data:
        degree = edu.get('degree', '')
        institution = edu.get('institution', '')
        location = edu.get('location', '')
        start = format_date(edu.get('startDate', ''))
        end = format_date(edu.get('endDate', ''))
        advisor = edu.get('advisor', '')
        description = edu.get('description', '')
        
        # Format date range
        date_range = f"{start} - {end}"
        
        content += f"""    <div class="education-item">
      <h3>{degree}</h3>
      <p class="institution">{institution}</p>
      <p class="date">{date_range}</p>
"""
        
        if advisor:
            content += f"      <p>Advisor: Prof. {advisor}</p>\n"
        
        if description:
            content += f"      <p>Focus: {description}</p>\n"
        
        content += "    </div>\n"
    
    content += """  </section>
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
    
    # Generate about page
    about_content = generate_about()
    about_path = docs_dir / 'about.md'
    with open(about_path, 'w') as f:
        f.write(about_content)
    print(f"✅ About page generated: {about_path}")
    
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
    
    # Generate service page
    service_content = generate_service()
    service_path = docs_dir / 'service.md'
    with open(service_path, 'w') as f:
        f.write(service_content)
    print(f"✅ Leadership & Service page generated: {service_path}")
    
    print("\n🎉 All website pages generated successfully!")


if __name__ == '__main__':
    main()
