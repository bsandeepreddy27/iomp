# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cases/', views.case_list, name='case_list'),
    path('cases/add/', views.add_case, name='add_case'),
    path('home', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('cases/<int:case_id>/edit/', views.edit_case, name='edit_case'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.custom_logout, name='logout'),
]

