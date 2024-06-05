# myapp/scripts/add_judges.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caseproject.settings')
django.setup()

from myapp.models import Judge

judge_names = ["Justice Arvind Kumar", "Justice Manjula Chellur", "Justice Dipak Misra", "Justice Ranjan Gogoi", "Justice Madan Lokur"]

for name in judge_names:
    Judge.objects.get_or_create(name=name)
