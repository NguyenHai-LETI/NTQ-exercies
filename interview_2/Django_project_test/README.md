# Django Project

Đây là một dự án Django với Django REST Framework và JWT authentication.

## Cài đặt

1. Tạo virtual environment:
```bash
python -m venv venv
```

2. Kích hoạt virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Chạy migrations:
```bash
python manage.py migrate
```

5. Tạo superuser (tùy chọn):
```bash
python manage.py createsuperuser
```

6. Chạy server:
```bash
python manage.py runserver
```

## Cấu trúc dự án

- `myproject/`: Thư mục chính của dự án Django
- `myapp/`: Ứng dụng Django
- `requirements.txt`: Danh sách các dependencies
- `.gitignore`: File loại trừ các file không cần thiết khỏi Git

## Lưu ý

- Thư mục `venv/` đã được loại trừ khỏi Git repository
- Để cài đặt lại môi trường, chỉ cần chạy `pip install -r requirements.txt` 