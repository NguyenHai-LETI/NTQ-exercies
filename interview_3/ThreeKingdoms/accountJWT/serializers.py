from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        # tạo user với ps được mã hóa
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# Serializer để xác thực người dùng khi đăng nhập
# Chúng ta không cần tạo serializer riêng vì SimpleJWT đã cung cấp sẵn
