from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('', views.soldier_view, name='soldier_list'),
    
    # Class-based view
    path('cbv/', views.SoldierListView.as_view(), name='soldier_list_cbv'),
]