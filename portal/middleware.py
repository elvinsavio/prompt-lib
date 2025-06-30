from django.shortcuts import redirect
from django.urls import reverse

class AuthTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to login page without token
        if request.path == reverse('login'):
            return self.get_response(request)
        
        # Check for 'auth_token' in session or cookies
        auth_token = request.session.get('auth_token') or request.COOKIES.get('auth_token')
        if not auth_token:
            return redirect(reverse('login'))
        return self.get_response(request)
