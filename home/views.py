from django.shortcuts import render

# Create your views here.

# from .models.custom_text import CustomText
from .models.home_page import HomePage


def home(request):
    packages = [
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        # 'customtext': CustomText.objects.first(),
        'customtext': 'test',
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
