#!/usr/bin/env python3
"""
Generate CV for template t2 (ModernCV template)
Generate LaTeX CV sections from JSON data
"""
import json
from datetime import datetime
from pathlib import Path


def escape_latex(text):
    """Escape special LaTeX characters"""
    if not isinstance(text, str):
        return text

    # Order matters! Do backslash first, but we'll handle it differently
    # First, temporarily replace backslashes
    text = text.replace('\\', 'BACKSLASHTEMP')

    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
    }

    for char, replacement in replacements.items():
        text = text.replace(char, replacement)

    # Now replace backslashes
    text = text.replace('BACKSLASHTEMP', r'\textbackslash{}')

    return text


def format_date_range(start, end):
    """Format date range for CV"""
    if end.lower() == "present":
        return f"{start[:4]}--Present"
    return f"{start[:4]}--{end[:4]}"


def format_authors(authors, highlight_name="Wang, Hanchen David"):
    """Format author list, bolding the highlighted name"""
    formatted = []
    for author in authors:
        if author == highlight_name:
            formatted.append(f"\\textbf{{{author}}}")
        else:
            formatted.append(author)
    return ", ".join(formatted)


def generate_header(data):
    """Generate header.tex"""
    personal = data["personal"]
    social = personal["social"]

    content = f"""\\firstname{{{personal["firstName"]}}}
\\familyname{{{personal["lastName"]}}}
\\email{{{personal["email"]}}}
\\title{{{personal["title"]}}}
\\address{{{personal["address"]["line1"]}}}{{{personal["address"]["line2"]}}}{{}}
\\social[linkedin]{{{social["linkedin"]}}}
\\social[github]{{{social["github"]}}}
"""

    # Add phone number if it exists
    if personal.get("phone"):
        content += f"\\mobile{{{personal['phone']}}}\n"

    return content


def generate_education(data):
    """Generate 20_education.tex"""
    content = "\\section{Education}\n\n"

    for edu in data["education"]:
        date_range = format_date_range(edu["startDate"], edu["endDate"])
        description = edu["description"] if edu["description"] else ""
        if edu["advisor"]:
            description = f"Advisor: {edu['advisor']}. {description}" if description else f"Advisor: {edu['advisor']}"

        # Only output description if not empty
        if description:
            content += f"""\\cventry{{{date_range}}}{{{escape_latex(edu["degree"])}}}{{{escape_latex(edu["institution"])}}}{{{escape_latex(edu["location"])}}}{{}}{{
{escape_latex(description)}
}}

"""
        else:
            content += f"""\\cventry{{{date_range}}}{{{escape_latex(edu["degree"])}}}{{{escape_latex(edu["institution"])}}}{{{escape_latex(edu["location"])}}}{{}}{{}}

"""
    return content


def generate_experience(data):
    """Generate 10_professional_experience.tex"""
    content = "\\section{Professional Experience}\n\n"

    for exp in data["experience"]:
        date_range = format_date_range(exp["startDate"], exp["endDate"])

        highlights = ""
        if exp["highlights"]:
            highlights = "\\begin{itemize}\n"
            for highlight in exp["highlights"]:
                highlights += f"  \\item {escape_latex(highlight)}\n"
            highlights += "\\end{itemize}"

        content += f"""\\cventry{{{date_range}}}{{{escape_latex(exp["title"])}}}{{{escape_latex(exp["organization"])}}}{{{escape_latex(exp["location"])}}}{{}}{{
{highlights}
}}

"""
    return content


def generate_research(data):
    """Generate research section (part of miscellaneous)"""
    content = "\\section{Research Experience}\n\n"

    for research in data["research"]:
        date_range = format_date_range(
            research["startDate"], research["endDate"]
        )

        # Format collaborators
        collab_text = ""
        if research["collaborators"]:
            collab_text = f"Collaborators: {', '.join(research['collaborators'])}"

        # Format description
        desc_items = ""
        if research["description"]:
            desc_items = "\\begin{itemize}\n"
            for desc in research["description"]:
                desc_items += f"  \\item {escape_latex(desc)}\n"
            desc_items += "\\end{itemize}"

        content += f"""\\cventry{{{date_range}}}{{{escape_latex(research["title"])}}}{{{collab_text}}}{{}}{{}}{{
{desc_items}
}}

"""
    return content


def generate_publications(data):
    """Generate publications section"""
    content = "\\section{Publications}\n\n"

    for i, pub in enumerate(data["publications"], 1):
        authors = format_authors(pub["authors"])
        status = f", {pub['status']}" if pub.get("status") else ""

        content += f"""\\cvitem{{{pub["year"]}}}{{
{authors}. 
\\textit{{{pub["title"]}}}.
{pub["venue"]}, {pub["month"]} {pub["year"]}{status}.
}}

"""
    return content


def generate_skills(data):
    """Generate skills section"""
    content = "\\section{Skills}\n\n"

    skills = data["skills"]
    content += f"\\cvitem{{Programming}}{{{', '.join(skills['programming'])}}}\n"
    content += f"\\cvitem{{Frameworks}}{{{', '.join(skills['frameworks'])}}}\n"
    content += f"\\cvitem{{Tools}}{{{', '.join(skills['tools'])}}}\n"
    content += f"\\cvitem{{Domains}}{{{', '.join(skills['domains'])}}}\n"

    return content


def generate_service(data):
    """Generate leadership and service section"""
    content = "\\section{Leadership and Service}\n\n"

    for service in data["service"]:
        date_range = format_date_range(service["startDate"], service["endDate"])

        # Format highlights
        highlights = ""
        if service["highlights"]:
            highlights = "\\begin{itemize}\n"
            for highlight in service["highlights"]:
                highlights += f"  \\item {escape_latex(highlight)}\n"
            highlights += "\\end{itemize}"

        content += f"""\\cventry{{{date_range}}}{{{escape_latex(service["title"])}}}{{{escape_latex(service["organization"])}}}{{{escape_latex(service["location"])}}}{{}}{{
{highlights}
}}

"""
    return content


def generate_miscellaneous(data):
    """Generate 30_miscellaneous.tex with research, publications, skills, and service"""
    content = generate_research(data)
    content += "\n"
    content += generate_publications(data)
    content += "\n"
    content += generate_service(data)
    content += "\n"
    content += generate_skills(data)

    return content


def main():
    # Load JSON data from separate files
    data_dir = Path(__file__).parent.parent / "data"

    with open(data_dir / "personal.json") as f:
        data = {
            "personal": json.load(f)
        }
    with open(data_dir / "education.json") as f:
        data["education"] = json.load(f)
    with open(data_dir / "employment.json") as f:
        data["experience"] = json.load(f)
    with open(data_dir / "research.json") as f:
        data["research"] = json.load(f)
    with open(data_dir / "publications.json") as f:
        data["publications"] = json.load(f)
    with open(data_dir / "skills.json") as f:
        data["skills"] = json.load(f)
    with open(data_dir / "service.json") as f:
        data["service"] = json.load(f)

    # Output directory
    output_dir = Path(__file__).parent.parent / "cv_template-main" / "src"

    # Generate header
    header_path = output_dir / "common" / "sections" / "header.tex"
    header_path.parent.mkdir(parents=True, exist_ok=True)
    with open(header_path, "w") as f:
        f.write(generate_header(data))
    print(f"✅ Generated: {header_path}")

    # Generate CV sections
    cv_sections_dir = output_dir / "cv" / "lang" / "en" / "sections"
    cv_sections_dir.mkdir(parents=True, exist_ok=True)

    sections = {
        "10_professional_experience.tex": generate_experience(data),
        "20_education.tex": generate_education(data),
        "30_miscellaneous.tex": generate_miscellaneous(data),
    }

    for filename, content in sections.items():
        section_path = cv_sections_dir / filename
        with open(section_path, "w") as f:
            f.write(content)
        print(f"✅ Generated: {section_path}")

    print("\n🎉 All LaTeX files generated successfully!")
    print("Run './build-cv-local.sh' to build the PDF")


if __name__ == "__main__":
    main()
