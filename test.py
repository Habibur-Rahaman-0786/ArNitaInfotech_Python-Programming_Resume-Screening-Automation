import unittest

from candidate_extractor import extract_email, extract_phone
from skill_extractor import extract_skills
from ranking_system import calculate_score

class TestResumeScreening(unittest.TestCase):
    def test_email_extraction(self):
        text = "My email is johnsmith@gmail.com"
        expected = "johnsmith@gmail.com"

        result = extract_email(text)

        self.assertEqual(result, expected)

    def test_phone_extraction(self):
        text = "Contact me at 9876543210"
        expected = "9876543210"

        result = extract_phone(text)

        self.assertEqual(result, expected)

    def test_skill_extraction(self):
        text = "I know Python, SQL and Machine Learning"
        expected = ["python", "sql", "machine learning"]

        result = extract_skills(text)

        for skill in expected:
            self.assertIn(skill, result)

    def test_score_calculation(self):
        skills = ["python", "sql"]
        result = calculate_score(skills)

        self.assertTrue(result >= 0)

if __name__ == "__main__":
    unittest.main()