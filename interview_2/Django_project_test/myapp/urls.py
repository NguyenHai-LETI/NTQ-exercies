from django.urls import path, include
from . import views, auth_views
from rest_framework.routers import DefaultRouter

#router for ViewSets
router = DefaultRouter()
router.register(r'items', views.ItemViewSet) # đăng kí url /items thực hiện CRUD

urlpatterns = [
    path('items-fbv/', views.item_list_fbv, name='item_list_fbv'),
    path('post-item-fbv/', views.item_create_fbv, name='post_item_fbv'),
    path('items-cbv/', views.ItemList.as_view(), name='item_list_cbv'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('public-items/', views.PublicItemList.as_view(), name='public_items'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/register/', auth_views.register_view, name='register'),
    path('api/', include(router.urls)),
]