from django.urls import path, include
from . import views, auth_views
from rest_framework.routers import DefaultRouter

#router for ViewSets
router = DefaultRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('items-api/', views.ItemList.as_view(), name='item_list_api'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('public-items/', views.PublicItemList.as_view(), name='public_items'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/register/', auth_views.register_view, name='register'),
    path('auth/refresh/', auth_views.refresh_token_view, name='refresh_token'),
    path('api/', include(router.urls)),
]