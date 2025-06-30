from django.shortcuts import redirect
from django.urls import reverse
import jwt
from django.conf import settings

EXCEPT_ROUTES = ('/login', '/static/')

class AuthTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if any(request.path.startswith(route) for route in EXCEPT_ROUTES):
            return self.get_response(request)

        token = request.COOKIES.get('token')
        print(f"Token: {token}")  # Debugging line to check the token value
        if not token:
            return redirect(reverse('login'))
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            request.user_payload = payload
            print(f"Payload: {payload}")  # Debugging line to check the payload
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return redirect('login')
        except jwt.InvalidTokenError:
            print("Invalid token")
            return redirect('login')
        
        return self.get_response(request)
