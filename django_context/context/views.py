from django.shortcuts import render
import datetime
def home(request):
    context = {
        'author': 'Rahim',
        'age': 15,
        'lst': ['python', 'is', 'fun'],
        'date':datetime.datetime.now(),
        'empty': '',
        'additional_lst': ['and', 'so', 'interesting'],
        'courses': [
            {'id': 1, 'name': 'Python', 'Fee': 5000},
            {'id': 2, 'name': 'Django', 'Fee': 10000},
            {'id': 3, 'name': 'Machine-learning', 'Fee': 20000}
        ]
    }
    return render(request, 'home.html', context)
