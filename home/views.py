from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-dev-125',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
