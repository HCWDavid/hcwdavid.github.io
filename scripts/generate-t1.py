#!/usr/bin/env python3
"""
Generate CV for template t1 (Simple clean template)
"""
import json
import sys
from pathlib import Path


def escape_latex(text):
    """Escape special LaTeX characters"""
    if not isinstance(text, str):
        return text

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

    text = text.replace('BACKSLASHTEMP', r'\textbackslash{}')
    return text


def format_date_range(start, end):
    """Format date range with full month names"""
    months = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec'
    }

    # Parse start date
    start_parts = start.split('-')
    start_year = start_parts[0]
    start_month = months.get(start_parts[1],
                             start_parts[1]) if len(start_parts) > 1 else ''
    start_formatted = f"{start_month} {start_year}"

    # Parse end date
    suffix = ""
    end_clean = end

    # Check for (Expected) or other parenthetical suffix
    if '(' in end:
        parts = end.split('(')
        end_clean = parts[0].strip()
        suffix = f" ({parts[1].strip(')')}"

    if end_clean.lower() == "present":
        end_formatted = f"Present{suffix}"
    elif '-' in end_clean:
        end_parts = end_clean.split('-')
        end_year = end_parts[0]
        end_month = months.get(end_parts[1],
                               end_parts[1]) if len(end_parts) > 1 else ''
        end_formatted = f"{end_month} {end_year}{suffix}"
    else:
        end_formatted = f"{end_clean}{suffix}"

    return f"{start_formatted} -- {end_formatted}"


def generate_simple_cv(data):
    """Generate complete CV using simple template"""

    # Read template
    template_path = Path(
        __file__
    ).parent.parent / "templates" / "simple" / "cv_template.tex"
    with open(template_path, 'r') as f:
        template = f.read()

    personal = data['personal']

    # Replace header
    template = template.replace(
        'HEADER_NAME', f"{personal['firstName']} {personal['lastName']}"
    )
    template = template.replace('HEADER_EMAIL', personal['email'])
    template = template.replace('HEADER_PHONE', personal.get('phone', ''))
    template = template.replace(
        'HEADER_LOCATION',
        f"{personal['address']['line1']}\\\\{personal['address']['line2']}"
    )
    template = template.replace(
        'HEADER_LINKEDIN', personal['social']['linkedin']
    )
    template = template.replace('HEADER_GITHUB', personal['social']['github'])

    # Generate Education
    edu_content = "\\cvsection{EDUCATION}\n\n"
    for edu in data['education']:
        date_range = format_date_range(edu['startDate'], edu['endDate'])
        # Use three minipage boxes to control alignment
        edu_content += "\\noindent\n"
        edu_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        edu_content += f"\\raggedright\\textbf{{{escape_latex(edu['institution'])}}}\n"
        edu_content += "\\end{minipage}%\n"
        edu_content += f"\\begin{{minipage}}[t]{{0.34\\textwidth}}\n"
        edu_content += f"\\centering\\textbf{{{escape_latex(edu['location'])}}}\n"
        edu_content += "\\end{minipage}%\n"
        edu_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        edu_content += f"\\raggedleft\\textbf{{{date_range}}}\n"
        edu_content += "\\end{minipage}\\\\[2pt]\n"
        edu_content += "\\begin{edulist}\n"

        # Add degree as first bullet
        edu_content += f"    \\item {escape_latex(edu['degree'])}"
        if edu.get('advisor'):
            edu_content += f", advised by {escape_latex(edu['advisor'])}\n"
        else:
            edu_content += "\n"

        # Add description/coursework as second bullet if exists
        if edu.get('description'):
            edu_content += f"    \\item \\textbf{{Highlighted Coursework:}} {escape_latex(edu['description'])}\n"

        # Add GPA if exists
        if edu.get('gpa'):
            edu_content += f"    \\item {escape_latex(edu['gpa'])}\n"

        edu_content += "\\end{edulist}\n"
        edu_content += "\n"

    # Generate Experience
    exp_content = "\\cvsection{Professional Experience}\n\n"
    for exp in data['experience']:
        date_range = format_date_range(exp['startDate'], exp['endDate'])
        # Use three minipage boxes to control alignment
        exp_content += "\\noindent\n"
        exp_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        exp_content += f"\\raggedright\\textbf{{{escape_latex(exp['title'])}}}\n"
        exp_content += "\\end{minipage}%\n"
        exp_content += f"\\begin{{minipage}}[t]{{0.34\\textwidth}}\n"
        exp_content += f"\\centering\\textbf{{{escape_latex(exp['location'])}}}\n"
        exp_content += "\\end{minipage}%\n"
        exp_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        exp_content += f"\\raggedleft\\textbf{{{date_range}}}\n"
        exp_content += "\\end{minipage}\\\\[2pt]\n"
        exp_content += f"\\textit{{{escape_latex(exp['organization'])}}}\n"
        if exp.get('highlights'):
            exp_content += "\\begin{itemize}\n"
            for highlight in exp['highlights']:
                exp_content += f"    \\item {escape_latex(highlight)}\n"
            exp_content += "\\end{itemize}\n"
        exp_content += "\n"

    # Generate Research
    research_content = "\\cvsection{Research Experience}\n"
    for research in data['research']:
        date_range = format_date_range(
            research['startDate'], research['endDate']
        )
        research_content += f"\\textbf{{{escape_latex(research['title'])}}} \\hfill {date_range}\\\\\n"
        if research.get('collaborators'):
            collabs = ', '.join(research['collaborators'])
            research_content += f"\\textit{{Collaborators: {escape_latex(collabs)}}}\n"
        if research.get('description'):
            research_content += "\\begin{itemize}\n"
            for desc in research['description']:
                research_content += f"    \\item {escape_latex(desc)}\n"
            research_content += "\\end{itemize}\n"
        research_content += "\n"

    # Generate Publications
    pub_content = "\\cvsection{Publications}\n"
    pub_content += "\\begin{enumerate}\n"
    for pub in data['publications']:
        # Escape authors first, then apply bold
        authors = ', '.join(pub['authors'])
        authors_escaped = escape_latex(authors)

        # Try to match both "Last, First" and "First Last" formats
        name_variants = [
            'Wang, Hanchen David', 'Hanchen David Wang', 'Wang, H. D.',
            'H. D. Wang', 'Wang, H.', 'H. Wang'
        ]

        for variant in name_variants:
            escaped_variant = escape_latex(variant)
            if escaped_variant in authors_escaped:
                authors_escaped = authors_escaped.replace(
                    escaped_variant, '\\textbf{' + escaped_variant + '}'
                )
                break

        status = f" ({pub['status']})" if pub.get('status') else ""
        pub_content += f"    \\item {authors_escaped}. \\textit{{{escape_latex(pub['title'])}}}. {escape_latex(pub['venue'])}, {pub['year']}{escape_latex(status)}.\n"
    pub_content += "\\end{enumerate}\n"

    # Generate Skills
    skills = data['skills']
    skills_content = "\\cvsection{Skills}\n"
    skills_content += f"\\textbf{{Programming:}} {escape_latex(', '.join(skills['programming']))}\\\\\n"
    skills_content += f"\\textbf{{Frameworks:}} {escape_latex(', '.join(skills['frameworks']))}\\\\\n"
    skills_content += f"\\textbf{{Tools:}} {escape_latex(', '.join(skills['tools']))}\\\\\n"
    skills_content += f"\\textbf{{Domains:}} {escape_latex(', '.join(skills['domains']))}\n"

    # Generate Awards
    awards_content = "\\cvsection{Awards}\n"
    awards_content += "\\begin{itemize}\n"
    for award in data['awards']:
        awards_content += f"    \\item \\textbf{{{escape_latex(award['title'])}:}} {escape_latex(award['description'])}\n"
    awards_content += "\\end{itemize}\n"

    # Generate Leadership and Service
    service_content = "\\cvsection{Leadership and Service}\n\n"
    for service in data['service']:
        date_range = format_date_range(service['startDate'], service['endDate'])
        # Use three minipage boxes to control alignment with linespread
        service_content += "\\vspace{3pt}\n"
        service_content += "\\noindent\n"
        service_content += "{\\linespread{0.85}\\selectfont%\n"
        service_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        service_content += f"\\raggedright\\textbf{{{escape_latex(service['title'])}}}\n"
        service_content += "\\end{minipage}%\n"
        service_content += f"\\begin{{minipage}}[t]{{0.34\\textwidth}}\n"
        service_content += f"\\centering\\textbf{{{escape_latex(service['location'])}}}\n"
        service_content += "\\end{minipage}%\n"
        service_content += f"\\begin{{minipage}}[t]{{0.33\\textwidth}}\n"
        service_content += f"\\raggedleft\\textbf{{{date_range}}}\n"
        service_content += "\\end{minipage}\\par}%\n"
        service_content += "\\vspace{1pt}\n"
        service_content += f"\\textit{{{escape_latex(service['organization'])}}}\n"
        if service.get('highlights'):
            service_content += "\\begin{itemize}\n"
            for highlight in service['highlights']:
                # Handle both string and dict formats
                if isinstance(highlight, str):
                    service_content += f"    \\item {escape_latex(highlight)}\n"
                elif isinstance(highlight, dict):
                    # New structured format with date, notes, mentees
                    highlight_text = f"{highlight.get('date', '')}: {highlight.get('notes', '')}"
                    service_content += f"    \\item {escape_latex(highlight_text)}\n"
            service_content += "\\end{itemize}\n"
        service_content += "\n"

    # Replace content in template
    template = template.replace('EDUCATION_CONTENT', edu_content)
    template = template.replace('EXPERIENCE_CONTENT', exp_content)
    template = template.replace('RESEARCH_CONTENT', research_content)
    template = template.replace('PUBLICATIONS_CONTENT', pub_content)
    template = template.replace('SERVICE_CONTENT', service_content)
    template = template.replace('SKILLS_CONTENT', skills_content)
    template = template.replace('AWARDS_CONTENT', awards_content)

    return template


def main():
    # Load data
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
    with open(data_dir / "awards.json") as f:
        data["awards"] = json.load(f)

    # Generate simple CV
    cv_content = generate_simple_cv(data)

    # Write to template directory
    output_path = Path(
        __file__
    ).parent.parent / "templates" / "simple" / "cv.tex"
    with open(output_path, 'w') as f:
        f.write(cv_content)

    print(f"✅ Generated: {output_path}")


if __name__ == "__main__":
    main()
