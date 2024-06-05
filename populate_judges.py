# populate_judges.py

import os
import django
import datetime

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caseproject.settings')
django.setup()

from myapp.models import Judge

# Judge details
judges = [
    {
        "name": "Dhananjaya Y. Chandrachud",
        "gender": "Male",
        "date_of_appointment": "2016-05-13",
        "becomes_cji_on": "2022-11-09",
        "date_of_retirement": "2024-11-10",
        "tenure_length": "8 years, 182 days",
        "tenure_length_as_cji": "2 years, 2 days",
        "parent_high_court": "Bombay"
    },
    {
        "name": "Sanjiv Khanna",
        "gender": "Male",
        "date_of_appointment": "2019-01-18",
        "becomes_cji_on": "2024-11-11",
        "date_of_retirement": "2025-05-13",
        "tenure_length": "6 years, 116 days",
        "tenure_length_as_cji": "184 days",
        "parent_high_court": "Delhi"
    },
    # Add remaining judge details here...
]

# Function to convert string dates to datetime.date objects
def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

# Populate the database with judge details
for judge_data in judges:
    judge = Judge(
        name=judge_data["name"],
        gender=judge_data["gender"],
        date_of_appointment=str_to_date(judge_data["date_of_appointment"]),
        becomes_cji_on=str_to_date(judge_data["becomes_cji_on"]) if judge_data["becomes_cji_on"] else None,
        date_of_retirement=str_to_date(judge_data["date_of_retirement"]),
        tenure_length=judge_data["tenure_length"],
        tenure_length_as_cji=judge_data["tenure_length_as_cji"] if judge_data["tenure_length_as_cji"] else None,
        parent_high_court=judge_data["parent_high_court"]
    )
    judge.save()
