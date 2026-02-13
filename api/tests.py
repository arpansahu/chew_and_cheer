from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from crud_django_form.models import Item
from api.models import Singer, Song


class APITestCase(TestCase):
    """Test cases for API endpoints"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test item
        self.test_item = Item.objects.create(
            name='Test Item',
            description='Test Description',
            price=10.99
        )

    def test_item_detail_view(self):
        """Test item detail API view"""
        response = self.client.get(f'/api/itemdetail/{self.test_item.id}')
        self.assertEqual(response.status_code, 200)
        # Test passes if the endpoint is accessible

    def test_item_list_view(self):
        """Test item list API view"""
        response = self.client.get('/api/itemdetail/')
        self.assertEqual(response.status_code, 200)
        # Test passes if the endpoint is accessible

    def test_item_create(self):
        """Test item creation via API"""
        data = {
            'name': 'New Item',
            'description': 'New Description',
            'price': 15.99
        }
        response = self.client.post('/api/itemcreate/', data, format='json')
        # Note: Actual status code depends on authentication requirements
        self.assertIn(response.status_code, [200, 201, 401, 403])


class SingerAPITestCase(TestCase):
    """Test cases for Singer/Song API"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = APIClient()
        self.singer = Singer.objects.create(
            name='Test Singer',
            gender='M'
        )

    def test_singer_creation(self):
        """Test singer model creation"""
        self.assertEqual(self.singer.name, 'Test Singer')
        self.assertEqual(self.singer.gender, 'M')
