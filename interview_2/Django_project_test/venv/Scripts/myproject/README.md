# Django REST Framework Project

Dự án demo đầy đủ các tính năng cơ bản của Django REST Framework với các yếu tố sau:

## ✅ Các yếu tố đã triển khai:

### 1. Class-based View và Function-based View
- **Function-based View**: `item_list()` - Trả về JSON response
- **Class-based View**: `ItemList(APIView)`, `ItemDetail(APIView)`, `PublicItemList(APIView)`

### 2. Authentication và Authorization
- **JWT Authentication**: Sử dụng `rest_framework_simplejwt`
- **Multiple Permission Levels**:
  - `AllowAny`: Public API không cần authentication
  - `IsAuthenticatedOrReadOnly`: Đọc cho tất cả, ghi cho user đã đăng nhập
  - `IsAuthenticated`: Chỉ cho user đã đăng nhập

### 3. Serializers, API View, ViewSet, Router
- **Serializer**: `ItemSerializer` (ModelSerializer)
- **APIView**: `ItemList`, `ItemDetail`, `PublicItemList`
- **ViewSet**: `ItemViewSet` với custom action
- **Router**: `DefaultRouter` cho ViewSet

### 4. Permissions & Throttling
- **Permissions**: `IsAuthenticated`, `IsAuthenticatedOrReadOnly`, `AllowAny`
- **Throttling**: `UserRateThrottle` với giới hạn 1000 requests/day (đã tắt cho development)

### 5. Django REST Framework
- Cấu hình đầy đủ trong `settings.py`
- JWT Authentication
- Throttling
- Permissions

### 6. Unittest
- `tests.py`: Test cho tất cả các view
- `test_auth.py`: Test cho authentication

## 🚀 Cách cài đặt và chạy:

### 1. Clone repository:
```bash
git clone <repository-url>
cd Django_project_test
```

### 2. Tạo virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

### 4. Chạy migrations:
```bash
cd venv/Scripts/myproject
python manage.py migrate
```

### 5. Tạo superuser (optional):
```bash
python manage.py createsuperuser
```

### 6. Chạy server:
```bash
python manage.py runserver
```

## 📋 Các endpoint có sẵn:

### Public Endpoints (Không cần authentication):
- `GET /` - Home page với danh sách endpoints
- `GET /api/items/` - Danh sách items (FBV)
- `GET /api/items-api/` - Danh sách items (CBV)
- `GET /api/public-items/` - Public API
- `GET /api/items/{id}/` - Chi tiết item (đọc)

### Authentication Endpoints:
- `POST /api/auth/register/` - Đăng ký user
- `POST /api/auth/login/` - Đăng nhập
- `POST /api/auth/refresh/` - Refresh token

### Protected Endpoints (Cần authentication):
- `GET /api/api/items/` - Danh sách items (ViewSet)
- `POST /api/api/items/` - Tạo item mới
- `PUT /api/items/{id}/` - Cập nhật item
- `GET /api/api/items/{id}/detail_info/` - Custom action

### Admin Panel:
- `GET /admin/` - Django Admin Panel

## 🧪 Test Authentication:

### Đăng ký user:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123", "email": "test@example.com"}'
```

### Đăng nhập:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Sử dụng token:
```bash
curl -X GET http://127.0.0.1:8000/api/api/items/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🧪 Chạy tests:
```bash
python manage.py test
```

## 📁 Cấu trúc dự án:

```
myproject/
├── myapp/
│   ├── models.py          # Item model
│   ├── serializers.py     # ItemSerializer
│   ├── views.py          # Views (FBV, CBV, ViewSet)
│   ├── auth_views.py     # Authentication views
│   ├── urls.py           # URL patterns
│   ├── tests.py          # API tests
│   ├── test_auth.py      # Authentication tests
│   └── admin.py          # Admin configuration
├── myproject/
│   ├── settings.py       # Django settings với DRF config
│   └── urls.py          # Main URL patterns
├── requirements.txt      # Dependencies
├── .gitignore          # Git ignore file
└── README.md           # Hướng dẫn này
```

## 🔧 Cấu hình quan trọng:

### REST_FRAMEWORK settings:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### JWT Settings:
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

## 🧪 Test Cases:

Dự án bao gồm các test case cho:
- Function-based Views
- Class-based Views
- ViewSets
- Authentication (đăng ký, đăng nhập)
- Permissions (với và không có authentication)
- Custom actions
- Error handling

## 📝 License:

MIT License

## 👥 Contributing:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Tất cả các yếu tố cơ bản của Django REST Framework đã được triển khai và test đầy đủ! 