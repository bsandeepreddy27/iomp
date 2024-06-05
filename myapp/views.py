# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .models import Case
from .forms import CaseForm

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(request, 'homecase.html')

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_list.html', {'cases': cases})

def add_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'add_case.html', {'form': form})

def edit_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    
    if request.method == 'POST':
        # Handle form submission and update the case in MySQL
        # Redirect to case list page or show a success message
        pass  # Placeholder for POST request handling
    
    # Render the edit_case.html template for GET requests
    return render(request, 'edit_case.html', {'case': case})


