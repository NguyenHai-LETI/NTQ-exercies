from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item


class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = Item.objects.create(name="Test Item", description="This is a test item.")
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
    def test_item_list_fbv(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Item")
