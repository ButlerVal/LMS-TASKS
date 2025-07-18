def format_txt_resume(data):
    lines = []
    # Personal Info
    lines.append(f"{data['personal_info']['name'].upper()}")
    lines.append("=" * len(data['personal_info']['name']))
    lines.append(f"Email: {data['personal_info']['email']}")
    lines.append(f"Phone: {data['personal_info']['phone']}")
    lines.append(f"Address: {data['personal_info']['address']}")
    lines.append("\n")

    # Education
    lines.append("EDUCATION")
    lines.append("-" * 9)
    for edu in data['education']:
        lines.append(f"{edu['degree']}")
        lines.append(f"{edu['institution']} | {edu['year']}")
        lines.append("")
    lines.append("")

    # Experience
    lines.append("EXPERIENCE")
    lines.append("-" * 10)
    for exp in data['experience']:
        lines.append(f"{exp['title']} | {exp['company']}, {exp['location']}")
        lines.append(f"{exp['duration']}")
        for resp in exp['responsibilities']:
            lines.append(f"- {resp}")
        lines.append("")
    lines.append("")

    # Skills
    lines.append("SKILLS")
    lines.append("-" * 6)
    lines.append(", ".join(data['skills']))
    lines.append("")

    return "\n".join(lines)

def format_md_resume(data):
    lines = []
    # Personal Info
    lines.append(f"# {data['personal_info']['name']}")
    lines.append(f"**Email**: {data['personal_info']['email']} | **Phone**: {data['personal_info']['phone']} | **Address**: {data['personal_info']['address']}")
    lines.append("")

    # Education
    lines.append("## Education")
    for edu in data['education']:
        lines.append(f"### {edu['degree']}")
        lines.append(f"{edu['institution']} | {edu['year']}")
        lines.append("")
    lines.append("")

    # Experience
    lines.append("## Experience")
    for exp in data['experience']:
        lines.append(f"### {exp['title']} | {exp['company']}, {exp['location']}")
        lines.append(f"*{exp['duration']}*")
        for resp in exp['responsibilities']:
            lines.append(f"- {resp}")
        lines.append("")
    lines.append("")

    # Skills
    lines.append("## Skills")
    lines.append(", ".join(data['skills']))

    return "\n".join(lines)