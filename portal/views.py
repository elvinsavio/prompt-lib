from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

import jwt

# Create your views here.
def login(request):
    # Simple login page (for demonstration)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {'username': username}, 
                settings.JWT_SECRET, 
                algorithm='HS256'
            )
            response = HttpResponse()
            response['HX-Redirect'] = '/'
            response.set_cookie(
                'token', 
                encoded_jwt, 
                httponly=True, 
                expires=datetime.today() + timedelta(hours=1),
                samesite='Lax',
                secure=request.is_secure(),
            )
            return response
        else:
            # Invalid credentials, show an error message
            return render(request, 'forms/login.html', {'error': 'Invalid credentials'})
      

    
    return render(request, 'login.html')


def landing(request):
    return render(request, 'landing.html')


def library_view_all(request):
    # Placeholder for library creation logic
    return render(request, 'library/all.html')

def library_new(request):
    # Placeholder for library creation logic
    return render(request, 'library/new.html')

def project_new(request):
    # Placeholder for project creation logic
    return render(request, 'project/new.html')