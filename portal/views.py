from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    # Simple login page (for demonstration)
    if request.method == "POST":
        # In a real app, validate credentials here
        request.session['auth_token'] = 'dummy_token'  # Set a dummy token
        return redirect('index')
    return render(request, 'login.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
