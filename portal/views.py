from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

import jwt

# Create your views here.
def login(request):
    # Simple login page (for demonstration)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f"User: {user}, Username: {username}, Password: {password}")
        if user is not None:
            encoded_jwt = jwt.encode(
                {'username': username}, 
                settings.JWT_SECRET, 
                algorithm='HS256'
            )

            response = HttpResponse(redirect('index'))
            response.set_cookie(
                'token', 
                encoded_jwt, 
                httponly=True, 
                expires=datetime.today() + timedelta(days=1),
                samesite='Lax',
                secure=request.is_secure(),  # ensures compatibility
            )
            return response
        else:
            # Invalid credentials, show an error message
            return render(request, 'login.html', {'error': 'Invalid credentials'})
      

    
    return render(request, 'login.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
