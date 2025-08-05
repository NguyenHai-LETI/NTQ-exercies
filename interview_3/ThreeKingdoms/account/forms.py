from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#Form đăng ký tùy chỉnh
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    # Form đăng nhập tùy chỉnh, kế thừa từ AuthenticationForm có sẵn của Django.
    pass