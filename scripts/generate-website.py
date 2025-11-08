#!/usr/bin/env python3
"""
Generate README.md (website content) from JSON data
"""
import json
from pathlib import Path


def format_date_range(start, end):
    """Format date range for display"""
    if end.lower() == "present":
        return f"{start[:7]} – Present"
    return f"{start[:7]} – {end[:7]}"


def format_month_year(year, month):
    """Format month and year"""
    return f"{month} {year}"


def generate_readme(data):
    """Generate complete README.md"""
    personal = data["personal"]

    # Header
    content = f"""# {personal["firstName"]} {personal["lastName"]}
Welcome! My name is David. I am currently a PhD student at Vanderbilt University working with Prof. [Meiyi Ma](https://meiyima.github.io) on eXplainable AI in Healthcare and Deep Learning research.

[LinkedIn](https://www.linkedin.com/in/{personal["social"]["linkedin"]}/) | [C.V.](./Resume.pdf) | [GitHub](https://github.com/{personal["social"]["github"]})

---

## **About Me**
{personal["bio"]}

---

## **Research Experience**

"""

    # Research projects
    for research in data["research"]:
        date_str = f"**{format_date_range(research['startDate'], research['endDate'])}**"
        collabs = ", ".join(research["collaborators"]
                            ) if research["collaborators"] else ""
        advisor_str = f"advised by {research['advisor']}" if research.get(
            "advisor"
        ) else ""

        if collabs and advisor_str:
            collab_line = f"Collaborators: {collabs}, {advisor_str}"
        elif collabs:
            collab_line = f"Collaborators: {collabs}"
        elif advisor_str:
            collab_line = advisor_str
        else:
            collab_line = ""

        content += f"""### **{research["title"]}**
{date_str}  
{collab_line}  

"""
        for desc in research["description"]:
            content += f"- {desc}\n"

        content += "\n---\n\n"

    # Publications
    content += """## **Publications**

"""

    for i, pub in enumerate(data["publications"], 1):
        authors = ", ".join(pub["authors"])
        # Bold the main author (you)
        authors = authors.replace(
            "Wang, Hanchen David", "**Wang, Hanchen David**"
        )

        status = f", {pub['status']}" if pub.get("status") else ""

        content += f"""{i}. {authors}  
   *{pub["title"]}.*  
   {pub["venue"]}, {format_month_year(pub["year"], pub["month"])}{status}.

"""

    content += """**More on [Publications](./publications.md)**

---

## PROJECT EXPERIENCE (Explain in Details): 

"""

    # Projects
    for project in data["projects"]:
        tech_str = ", ".join(project["technologies"])
        content += f"""**{project["title"]}:** _({project["date"]})_

[{project["title"]}]({project["links"][0]["url"]}): {project["description"]}

_Categories_: {tech_str}

"""
        if project != data["projects"][-1]:
            content += "\n"

    # Work Experience
    content += """
## WORK EXPERIENCE:

"""

    for exp in data["experience"]:
        if exp["type"] == "research":
            continue  # Skip research positions, they're in research section

        date_str = f"_({format_date_range(exp['startDate'], exp['endDate'])})_"
        content += f"""**{exp["title"]}** {date_str}

@{exp["organization"]}
"""
        for i, highlight in enumerate(exp["highlights"], 1):
            content += f"{i}. {highlight}\n"

        content += "\n"

    return content


def main():
    # Load JSON data
    json_path = Path(__file__).parent.parent / "data" / "cv-content.json"
    with open(json_path, "r") as f:
        data = json.load(f)

    # Generate README
    content = generate_readme(data)

    # Write to docs/index.md (for GitHub Pages)
    docs_path = Path(__file__).parent.parent / "docs"
    docs_path.mkdir(exist_ok=True)
    
    index_path = docs_path / "index.md"
    with open(index_path, "w") as f:
        f.write(content)

    print(f"✅ Generated: {index_path}")
    print("🎉 Website content updated!")


if __name__ == "__main__":
    main()
