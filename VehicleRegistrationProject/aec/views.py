from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return HttpResponse("<h1>Index page</h1>")

# def login(request):
#     return render(request, 'aec/admin-login.html')

def login(request):
    
    user_login_form = forms.login_form()

    if request.method == 'POST':
        user_login_form = forms.login_form(request.POST)

        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']

            print("Credentials are:")
            print("Username "+ username)
            print("Password " + password)

    return render(request, 'aec/admin-login.html', {'form': user_login_form})
