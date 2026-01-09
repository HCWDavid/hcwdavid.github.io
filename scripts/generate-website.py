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
            authors_str = authors_str.replace(
                variation, f"<strong>{variation}</strong>"
            )
            break

    return authors_str


def generate_homepage():
    """Generate the homepage (index.md)."""
    research_data = load_json('research.json')
    publications_data = load_json('publications.json')
    employment_data = load_json('employment.json')
    education_data = load_json('education.json')

    # Get latest items
    latest_research = research_data[0] if research_data else None

    # Get latest publication with "Accepted" status
    latest_publication = None
    for pub in publications_data:
        status = pub.get('status', '')
        if status.startswith('Accepted'):
            latest_publication = pub
            break

    latest_position = employment_data[0] if employment_data else None

    content = """---
layout: default
---

<style>
  @keyframes typing {
    0%, 100% { max-width: 0; }
    20%, 80% { max-width: 100%; }
  }
  
  @keyframes blink-caret {
    from, to { border-color: transparent; }
    50% { border-color: #4a9eff; }
  }
  
  .typing-name {
    display: inline-block;
    overflow: hidden;
    border-right: 3px solid #4a9eff;
    white-space: nowrap;
    max-width: fit-content;
    animation: 
      typing 6s steps(20, end) infinite,
      blink-caret .75s step-end infinite;
  }
  
  .profile-header h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
  }
  
  .profile-header .typing-name {
    display: inline-block;
  }
  
  .profile-header {
    padding: 20px 30px !important;
  }
  
  .profile-photo {
    margin-bottom: 15px !important;
    width: 180px !important;
    height: 180px !important;
  }
  
  .profile-header h1 {
    margin: 5px 0 5px 0 !important;
  }
  
  .profile-header .tagline {
    margin-bottom: 10px !important;
  }
  
  /* Fancy section headers */
  section h2 {
    font-family: 'Courier New', monospace;
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    margin-top: 0 !important;
    margin-bottom: 15px;
    position: relative;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 8px 12px;
    border-radius: 4px;
  }
  
  section h2::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
  
  /* Fancy content boxes */
  section {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 20px 20px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  section:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  .education-item, .highlight-item {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-left: 3px solid #4a9eff;
    padding: 15px 18px;
    margin-bottom: 15px;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  
  .education-item:hover, .highlight-item:hover {
    border-left-width: 5px;
    padding-left: 16px;
    background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%);
  }
  
  .education-item h3, .highlight-item h3 {
    color: #2c3e50;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 6px;
    margin-top: 0;
  }
  
  .highlight-item p {
    margin: 5px 0;
    line-height: 1.5;
    font-size: 14px;
  }
  
  .highlight-item p:last-child {
    margin-bottom: 0;
  }
  
  /* Make all section content more compact */
  section p {
    margin: 8px 0;
    line-height: 1.5;
    font-size: 14px;
  }
  
  section p:first-of-type {
    margin-top: 0;
  }
  
  section p:last-of-type {
    margin-bottom: 0;
  }
  
  .quick-links ul {
    list-style: none;
    padding: 0;
  }
  
  .quick-links li {
    margin-bottom: 10px;
  }
  
  .quick-links a {
    display: inline-block;
    padding: 8px 15px;
    background: linear-gradient(135deg, #4a9eff 0%, #357abd 100%);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s ease;
    font-weight: 500;
  }
  
  .quick-links a:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.3);
  }
</style>

<div class="about-page">
  <div class="profile-header">
    <img src="./assets/portfolio.png" alt="Hanchen David Wang" class="profile-photo">
    <h1><span class="typing-name">Hanchen David Wang</span></h1>
    <p class="tagline">{{ site.description }}</p>
    
    <!-- Social Links -->
    <div class="social-links-large">
      <a href="https://www.linkedin.com/in/hanchendavidwang/" target="_blank" title="LinkedIn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
        </svg>
        <span>LinkedIn</span>
      </a>
      <a href="./Resume.pdf" target="_blank" title="Curriculum Vitae">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
        </svg>
        <span>Curriculum Vitae</span>
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
    <h2>About Me</h2>
    <p>Welcome! My name is David. I am currently a PhD student at Vanderbilt University working with Prof. <a href="https://meiyima.github.io" target="_blank">Meiyi Ma</a> on <strong>eXplainable AI in Healthcare</strong> and <strong>Deep Learning research</strong>. Outside of research, I love staying active through workouts, expressing creativity through drawing, and exploring the outdoors. I'm also a big cat lover! Whether it's grabbing boba or coffee, I'm always up for a good conversation. ☕🧋</p>
  </section>

  <section class="interests">
    <h2>Research Interests</h2>
    <p>My research spans across multiple areas of artificial intelligence and computer science, with a focus on making AI systems more explainable, reliable, and beneficial for healthcare applications.</p>
    <p><strong>Key Areas:</strong> Explainable AI (XAI), Healthcare AI, Machine Learning, Physical Therapy & Motion Analysis, Nursing Education Simulations, Formal Verification, Multimodal Learning, Continual Learning</p>
  </section>

  <section class="education">
    <h2>Education</h2>
"""

    # Add education items from JSON
    for edu in education_data:
        degree = edu.get('degree', '')
        institution = edu.get('institution', '')
        start = format_date(edu.get('startDate', ''))
        end = format_date(edu.get('endDate', ''))
        advisor = edu.get('advisor', '')
        description = edu.get('description', '')

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

  <section class="recent-highlights">
    <h2>Recent Highlights</h2>
    
"""

    # Add latest research
    if latest_research:
        start = format_date(latest_research.get('startDate', ''))
        end = format_date(latest_research.get('endDate', 'Present'))
        title = latest_research.get('title', '')
        description = latest_research.get('description', [
            ''
        ])[0] if latest_research.get('description') else ''

        content += f"""    <div class="highlight-item">
      <h3>Latest Research</h3>
      <p><strong>{title}</strong> ({start} - {end})</p>
      <p>{description}</p>
    </div>

"""

    # Add recent publication
    if latest_publication:
        title = latest_publication.get('title', '')
        venue = latest_publication.get('venue', '')
        status = latest_publication.get('status', '')

        status_text = f" - {status}" if status else ""
        content += f"""    <div class="highlight-item">
      <h3>Recent Publication</h3>
      <p><strong>{title}</strong></p>
      <p>{venue}{status_text}</p>
    </div>

"""

    # Add current position
    if latest_position:
        start = format_date(latest_position.get('startDate', ''))
        end = format_date(latest_position.get('endDate', 'Present'))
        org = latest_position.get('organization', '')
        position_title = latest_position.get('title', '')
        highlights = latest_position.get('highlights', [])
        description = highlights[0] if highlights else ''

        content += f"""    <div class="highlight-item">
      <h3>Current Position</h3>
      <p><strong>{position_title} @ {org}</strong> ({start} - {end})</p>
      <p>{description}</p>
    </div>

"""

    content += """  </section>

  <section class="quick-links">
    <h2>Quick Links</h2>
    <ul>
      <li><a href="./publications.html">View my Publications</a></li>
      <li><a href="./projects.html">Check out my Projects</a></li>
      <li><a href="./service.html">Service</a></li>
    </ul>
  </section>
</div>

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
    google_scholar_url = personal_data.get('social', {}).get(
        'google_scholar', 'https://scholar.google.com'
    )

    content = """---
layout: default
title: Publications
---

<style>
  /* Fancy section styling */
  .publication-list {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 30px;
    margin-bottom: 25px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }
  
  .publication-item {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-left: 3px solid #4a9eff;
    padding: 15px 20px;
    margin-bottom: 20px;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  
  .publication-item:hover {
    border-left-width: 5px;
    padding-left: 18px;
    background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 10px 15px;
    border-radius: 4px;
  }
  
  h1::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
</style>

<h1>Publications</h1>

<p>A comprehensive list of my research publications in artificial intelligence, machine learning, and healthcare applications.</p>

<div class="publication-list">

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

        # Start publication item
        content += f"""<div class="publication-item">
{i}. """

        # Format the entry with title first (larger font, clickable if DOI available) then authors on next line
        doi = pub.get('doi', '')
        if doi:
            # Add https://doi.org/ prefix if not already present
            doi_url = doi if doi.startswith(
                'http'
            ) else f"https://doi.org/{doi}"
            content += f"<a href='{doi_url}' target='_blank' style='text-decoration: underline; color: #333; font-weight: 600; font-size: 1.1em;'>{title}</a>  \n"
        else:
            content += f"<span style='font-weight: 600; font-size: 1.1em;'>{title}</span>  \n"

        content += f"   <br>\n   {authors}  \n"

        if venue:
            content += f"   {venue}"
            if date:
                content += f", {date}"
            if status:
                content += f", {status}"
            content += ".  \n"

        # Add arXiv link if available (but not DOI since it's in the title now)
        arxiv = pub.get('arxiv', '')
        if arxiv:
            # Add https://arxiv.org/abs/ prefix if not already present
            arxiv_url = arxiv if arxiv.startswith(
                'http'
            ) else f"https://arxiv.org/abs/{arxiv}"
            content += f"   [arXiv]({arxiv_url})  \n"

        content += "</div>\n\n"

    content += """</div>

---

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

<style>
  /* Fancy section styling */
  .project-item {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 20px 20px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .project-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  .project-item h2 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    margin-top: 0;
    margin-bottom: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 8px 12px;
    border-radius: 4px;
  }
  
  .project-item h2::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
  
  h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 10px 15px;
    border-radius: 4px;
  }
  
  h1::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
</style>

<h1>Projects</h1>

<p>A collection of my software engineering and development projects, showcasing work across various technologies and domains.</p>

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
                filename = link_url.replace('./projects/',
                                            '').replace('.html', '.md')
                project_file = docs_dir / filename
                has_detail_page = project_file.exists()

        # If detail page exists, make title clickable; otherwise, just show as text
        if has_detail_page:
            content += f"""<div class="project-item">
<h2><a href="{link_url}" style="text-decoration: none; color: inherit;">{title}</a></h2>
<p><strong>{date}</strong></p>

<p>{description}</p>

<p><strong>Technologies:</strong> {technologies}</p>
</div>

"""
        else:
            content += f"""<div class="project-item">
<h2>{title}</h2>
<p><strong>{date}</strong></p>

<p>{description}</p>

<p><strong>Technologies:</strong> {technologies}</p>
</div>

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

<style>
  /* Fancy section styling */
  .service-item {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 20px 20px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .service-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  .service-item h2 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    margin-top: 0;
    margin-bottom: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 8px 12px;
    border-radius: 4px;
  }
  
  .service-item h2::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
  
  h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 10px 15px;
    border-radius: 4px;
  }
  
  h1::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
</style>

<h1>Leadership & Service</h1>

<p>My contributions to the academic community through mentoring, volunteering, and service activities.</p>

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

        content += f"""<div class="service-item">
<h2>{title}</h2>
<p><strong>{organization}</strong> | {location}<br>
<strong>{date_range}</strong></p>

"""

        # Add highlights as bullet points
        if highlights:
            content += "<ul>\n"
            for highlight in highlights:
                # Check if highlight is a dict (new structure) or string (old structure)
                if isinstance(highlight, dict):
                    date = highlight.get('date', '')
                    notes = highlight.get('notes', '')
                    mentees = highlight.get('mentees', [])

                    # If there are mentees with websites, append links to notes
                    if mentees:
                        mentee_links = []
                        for mentee in mentees:
                            name = mentee.get('name', '')
                            website = mentee.get('website', '')
                            if name and website:
                                mentee_links.append(f"[{name}]({website})")

                        if mentee_links:
                            notes += f" (Mentees: {', '.join(mentee_links)})"

                    content += f"<li><strong>{date}:</strong> {notes}</li>\n"
                else:
                    # Old string format
                    content += f"<li>{highlight}</li>\n"
            content += "</ul>\n"

        content += "</div>\n\n"

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


def generate_career():
    """Generate the career page."""
    employment_data = load_json('employment.json')

    content = """---
layout: default
title: Career
---

<style>
  /* Fancy section styling */
  .career-item {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 20px 20px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .career-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.15);
  }
  
  .career-item h2 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    margin-top: 0;
    margin-bottom: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 8px 12px;
    border-radius: 4px;
  }
  
  .career-item h2::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
  
  h1 {
    font-family: 'Courier New', monospace;
    color: #2c3e50;
    border-left: 4px solid #4a9eff;
    padding-left: 15px;
    background: linear-gradient(to right, rgba(74, 158, 255, 0.1) 0%, transparent 100%);
    padding: 10px 15px;
    border-radius: 4px;
  }
  
  h1::before {
    content: '>';
    color: #4a9eff;
    margin-right: 8px;
    font-weight: bold;
  }
</style>

<h1>Career</h1>

<p>My professional experience spanning research, teaching, and industry internships.</p>

"""

    for i, job in enumerate(employment_data, 1):
        title = job.get('title', '')
        organization = job.get('organization', '')
        location = job.get('location', '')
        start = format_date(job.get('startDate', ''))
        end = format_date(job.get('endDate', ''))
        highlights = job.get('highlights', [])

        # Format date range
        date_range = f"{start} - {end}" if start != end else start

        content += f"""<div class="career-item">
<h2>{title}</h2>
<p><strong>{organization}</strong> | {location}<br>
<strong>{date_range}</strong></p>

"""

        # Add highlights as bullet points
        if highlights:
            content += "<ul>\n"
            for highlight in highlights:
                content += f"<li>{highlight}</li>\n"
            content += "</ul>\n"

        content += "</div>\n\n"

    content += """
<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; border: 1px solid #dee2e6;">
  <p style="color: #495057; margin: 0;">
    Interested in working together? <a href="./Resume.pdf" style="color: #212529; font-weight: 600;">Download my CV</a>
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

    # Generate career page
    career_content = generate_career()
    career_path = docs_dir / 'career.md'
    with open(career_path, 'w') as f:
        f.write(career_content)
    print(f"✅ Career page generated: {career_path}")

    # Generate service page
    service_content = generate_service()
    service_path = docs_dir / 'service.md'
    with open(service_path, 'w') as f:
        f.write(service_content)
    print(f"✅ Leadership & Service page generated: {service_path}")

    print("\n🎉 All website pages generated successfully!")


if __name__ == '__main__':
    main()
