from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('register/', views.register_view, name='register_page'),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
]