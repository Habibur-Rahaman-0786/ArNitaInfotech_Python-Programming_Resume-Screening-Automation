from skills_database import skills_list

#Function to Extract Candidates Skills
def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill.lower() in text:
            found.append(skill)

    return list(set(found))