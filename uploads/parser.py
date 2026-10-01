import re
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

skills_db = [
"python","java","html","css","javascript",
"sql","machine learning","deep learning",
"flask","django","react","node"
]

def extract_text_from_pdf(path):
    return extract_text(path)

def extract_email(text):
    match = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", text)
    return match[0] if match else "Not Found"

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,12}\d", text)
    return match[0] if match else "Not Found"

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not Found"

def extract_skills(text):
    found = []
    for skill in skills_db:
        if skill.lower() in text.lower():
            found.append(skill)
    return found

def extract_education(text):
    education_keywords = [
    "bachelor","master","phd","bsc","msc",
    "computer science","software engineering"
    ]

    edu_found = []

    for word in education_keywords:
        if word in text.lower():
            edu_found.append(word)

    return edu_found