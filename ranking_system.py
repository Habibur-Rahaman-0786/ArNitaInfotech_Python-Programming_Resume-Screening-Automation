from skills_database import skills_list

#Function to Calculate Final Match Score
def calculate_score(found_skills):
    total = len(skills_list)
    score = (len(found_skills) / total) * 100

    return round(score, 2)