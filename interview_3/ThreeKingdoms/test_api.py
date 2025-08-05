#!/usr/bin/env python
"""
Script test cho API login và register
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/accounts/"

def test_register():
    """Test chức năng đăng ký"""
    print("=== Testing Register API ===")
    
    # Test data
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}register/", json=register_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 201:
            print("✅ Register API hoạt động tốt!")
        else:
            print("❌ Register API có lỗi!")
            
    except requests.exceptions.ConnectionError:
        print("❌ Không thể kết nối đến server. Hãy chạy: python manage.py runserver")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def test_login():
    """Test chức năng đăng nhập"""
    print("\n=== Testing Login API ===")
    
    # Test data
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}login/", json=login_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Login API hoạt động tốt!")
            # Lưu token để test các API khác
            data = response.json()
            if 'access_token' in data:
                print(f"Access Token: {data['access_token'][:20]}...")
        else:
            print("❌ Login API có lỗi!")
            
    except requests.exceptions.ConnectionError:
        print("❌ Không thể kết nối đến server. Hãy chạy: python manage.py runserver")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def test_invalid_login():
    """Test đăng nhập với thông tin sai"""
    print("\n=== Testing Invalid Login ===")
    
    # Test data sai
    login_data = {
        "username": "wronguser",
        "password": "wrongpass"
    }
    
    try:
        response = requests.post(f"{BASE_URL}login/", json=login_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 400:
            print("✅ Invalid login test hoạt động đúng!")
        else:
            print("❌ Invalid login test có lỗi!")
            
    except requests.exceptions.ConnectionError:
        print("❌ Không thể kết nối đến server.")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    print("Testing Three Kingdoms Authentication API")
    print("=" * 50)
    
    test_register()
    test_login()
    test_invalid_login()
    
    print("\n" + "=" * 50)
    print("Test hoàn thành!")
    print("\nĐể test giao diện web:")
    print("1. Chạy: python manage.py runserver")
    print("2. Mở: http://localhost:8000/")
    print("3. Click vào 'Đăng nhập' hoặc 'Đăng ký'") 