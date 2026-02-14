from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from crud_django_form.models import Item
import json


class CrudAjaxViewTest(TestCase):
    """Test cases for CRUD Ajax views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.item = Item.objects.create(
            name='Test Item',
            description='Test Description',
            price=10.99
        )

    def test_crud_view_requires_login(self):
        """Test that CRUD view requires login"""
        response = self.client.get(reverse('crud_ajax'))
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_crud_view_authenticated(self):
        """Test CRUD view with authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('crud_ajax'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_create_item_ajax(self):
        """Test creating item via Ajax"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('crud_ajax_create'),
            {
                'name': 'New Ajax Item',
                'description': 'Ajax Description',
                'price': 25.99
            }
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('item', data)
        self.assertEqual(data['item']['name'], 'New Ajax Item')
        self.assertEqual(float(data['item']['price']), 25.99)
        
        # Verify item was created in database
        self.assertTrue(Item.objects.filter(name='New Ajax Item').exists())

    def test_create_item_requires_login(self):
        """Test create requires login"""
        response = self.client.get(reverse('crud_ajax_create'))
        self.assertEqual(response.status_code, 302)

    def test_update_item_ajax(self):
        """Test updating item via Ajax"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('crud_ajax_update'),
            {
                'id': self.item.id,
                'name': 'Updated Item',
                'description': 'Updated Description',
                'price': 30.99
            }
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('item', data)
        self.assertEqual(data['item']['name'], 'Updated Item')
        
        # Verify item was updated in database
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.price, 30.99)

    def test_delete_item_ajax(self):
        """Test deleting item via Ajax"""
        self.client.login(username='testuser', password='testpass123')
        item_id = self.item.id
        response = self.client.get(
            reverse('crud_ajax_delete'),
            {'id': item_id}
        )
        # May redirect or return JSON
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 200:
            data = json.loads(response.content)
            self.assertIn('deleted', data)
            self.assertTrue(data['deleted'])

    def test_delete_nonexistent_item(self):
        """Test deleting non-existent item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('crud_ajax_delete'),
            {'id': 99999}
        )
        # Should handle gracefully (implementation dependent)
        self.assertIn(response.status_code, [200, 302, 404])



# ======================================================================
# AUTO-GENERATED TESTS - Django Test Enforcer
# Generated on: 2026-02-13 17:54:03
# These tests FAIL by default - implement them to make them pass!
# ======================================================================


from django.urls import reverse

class TestCrudAjaxClassBasedViews(TestCase):
    """Auto-generated tests for crud_ajax class-based views - IMPLEMENT THESE!"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.user.is_active = True
        self.user.save()
        self.client.force_login(self.user)

    def test_create_crud_user(self):
        """
        Test CreateCrudUser - AJAX create endpoint
        """
        response = self.client.get('/crud_ajax_class/ajax/crudclass/create/', {
            'name': 'Test Item',
            'description': 'Test Description',
            'price': '99.99'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('item', data)
        self.assertEqual(data['item']['name'], 'Test Item')

    def test_delete_crud_user(self):
        """
        Test DeleteCrudUser - AJAX delete endpoint
        """
        item = Item.objects.create(name='Delete Me', description='Test', price='10.00')
        response = self.client.get(f'/crud_ajax_class/ajax/crudclass/delete/?id={item.id}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('deleted', data)
        self.assertTrue(data['deleted'])
        self.assertFalse(Item.objects.filter(id=item.id).exists())

    def test_update_crud_user(self):
        """
        Test UpdateCrudUser - AJAX update endpoint
        """
        item = Item.objects.create(name='Old Name', description='Old Desc', price='10.00')
        response = self.client.get('/crud_ajax_class/ajax/crudclass/update/', {
            'id': item.id,
            'name': 'New Name',
            'description': 'New Desc',
            'price': '20.00'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('item', data)
        item.refresh_from_db()
        self.assertEqual(item.name, 'New Name')

