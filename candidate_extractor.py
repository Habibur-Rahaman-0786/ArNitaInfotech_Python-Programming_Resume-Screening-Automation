import re
import spacy

nlp = spacy.load("en_core_web_sm")

#Function to Extract Candidates Name
def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
        
    return "NOT FOUND"

#Function to Extract Candidates Email ID
def extract_email(text):
    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    if email:
        return email[0]
    
    return "NOT FOUND"

#Function to Extract Candidates Phone Number
def extract_phone(text):
    phone = re.findall(r"\+?\d[\d -]{8,12}\d", text)

    if phone:
        return phone[0]
    
    return "NOT FOUND"