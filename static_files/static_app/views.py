import select
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .djangoLoginForm import DjangoLoginForm 
from . forms import contactFrom
def link(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        select= request.POST.get('select')
        response_message = f"Received: Name - {name}, Email - {email}, 'select - {select}"
        return render(request, 'form.html', {'message': response_message})
    return render(request, 'form.html')
def loginForm(request):
    form = None  # Initialize form variable

    if request.method == 'POST':
        form = DjangoLoginForm(request.POST)
        if form.is_valid():
            return render(request, 'loginForm.html', {'form': form, 'message': 'Login successfully'})
    else:
        form = DjangoLoginForm()

    return render(request, 'loginForm.html', {'form': form})

def djangoForm(request):
    response_message = None

    if request.method == 'POST':
        form = contactFrom(request.POST, request.FILES)
        
        if form.is_valid():
            file = form.cleaned_data['file']
            upload_dir = os.path.join(settings.BASE_DIR, 'static_app', 'upload')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, file.name)

            with open( file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            response_message = f"Received: Name - {name}, Email - {email}, File - {file.name}"
    else:
        form = contactFrom()
    
    return render(request, 'djangoForm.html', {'form': form, 'message': response_message})
def dummy(request):
    data = {
        'info': [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus vel accusantium quis pariatur molestiae porro eius odio et labore et velit aut"
            },
            {
                "userId": 1,
                "id": 4,
                "title": "eum et est occaecati",
                "body": "ullam et saepe reiciendis voluptatem adipisci sit amet autem assumenda provident rerum culpa quis hic commodi nesciunt rem tenetur doloremque ipsam iure quis sunt voluptatem rerum illo velit"
            },
            {
                "userId": 1,
                "id": 5,
                "title": "nesciunt quas odio",
                "body": "repudiandae veniam quaerat sunt sed alias aut fugiat sit autem sed est voluptatem omnis possimus esse voluptatibus quis est aut tenetur dolor neque"
            }
        ]
    }
    return render(request, 'dummy.html', data)
