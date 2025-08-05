from django.urls import path
from .views import login_html

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import RegisterView, ProtectedView, LoginView

app_name = 'accountJWT'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login_html/', login_html, name='login_html'),
    # authen api
    path('protected/', ProtectedView.as_view(), name='protected'),
]
