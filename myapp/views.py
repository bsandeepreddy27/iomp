# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .models import Case
from .forms import CaseForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def home(request):
    return render(request, 'index.html', {'user': request.user})

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
@login_required
def home_view(request):
    return render(request, 'homecase.html', {'user': request.user})
    

@login_required
def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_list.html', {'cases': cases})

@login_required
def add_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'add_case.html', {'form': form})

@login_required
def edit_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    
    if request.method == 'POST':
        if request.POST.get('delete') == 'true':
            case.delete()
            return redirect('case_list')
        else:
            form = CaseForm(request.POST, instance=case)
            if form.is_valid():
                form.save()
                return redirect('case_list')
    else:
        form = CaseForm(instance=case)

    return render(request, 'edit_case.html', {'form': form})


@login_required
def delete_case(request, case_id):
    if request.method == 'POST':
        case = Case.objects.get(pk=case_id)
        case.delete()
        return redirect('case_list')
    return redirect('edit_case', case_id=case_id)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def logout(request):
    if request.method == 'POST':
        # Perform logout operation here
        return redirect('home')
    return render(request, 'logout.html')

@login_required
def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

