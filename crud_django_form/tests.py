from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item
from .forms import ItemCreation


class ItemModelTest(TestCase):
    """Test cases for Item model"""

    def setUp(self):
        self.item = Item.objects.create(
            name='Test Item',
            description='Test Description',
            price=10.99
        )

    def test_item_creation(self):
        """Test item is created correctly"""
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'Test Description')
        self.assertEqual(self.item.price, 10.99)

    def test_item_str(self):
        """Test item string representation"""
        self.assertEqual(str(self.item), 'Test Item')

    def test_item_fields(self):
        """Test item has all required fields"""
        self.assertTrue(hasattr(self.item, 'name'))
        self.assertTrue(hasattr(self.item, 'description'))
        self.assertTrue(hasattr(self.item, 'price'))


class ItemFormTest(TestCase):
    """Test cases for ItemCreation form"""

    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'name': 'New Item',
            'description': 'New Description',
            'price': 15.99
        }
        form = ItemCreation(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        """Test form with missing required fields"""
        form_data = {
            'name': 'New Item',
        }
        form = ItemCreation(data=form_data)
        self.assertFalse(form.is_valid())


class CrudDjangoFormViewsTest(TestCase):
    """Test cases for CRUD Django Form views"""

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

    def test_home_view_get(self):
        """Test home view GET request"""
        response = self.client.get(reverse('crudformhome'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_home_view_post_create_item(self):
        """Test home view POST request to create item"""
        data = {
            'name': 'New Item',
            'description': 'New Description',
            'price': 25.99
        }
        response = self.client.post(reverse('crudformhome'), data)
        self.assertEqual(Item.objects.count(), 2)
        self.assertTrue(Item.objects.filter(name='New Item').exists())

    def test_delete_item_view(self):
        """Test delete item view requires permission"""
        # Test without permission first
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('curdformdelete', kwargs={'id': self.item.id})
        )
        # Should redirect to logout since user doesn't have permission
        self.assertEqual(response.status_code, 302)
        # Item should still exist
        self.assertTrue(Item.objects.filter(id=self.item.id).exists())

    def test_update_item_view_get(self):
        """Test update item view GET request"""
        response = self.client.get(
            reverse('curdformupdate', kwargs={'id': self.item.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_update_item_view_post(self):
        """Test update item view POST request"""
        data = {
            'name': 'Updated Item',
            'description': 'Updated Description',
            'price': 30.99
        }
        response = self.client.post(
            reverse('curdformupdate', kwargs={'id': self.item.id}),
            data,
            follow=True
        )
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.price, 30.99)



# ======================================================================
# AUTO-GENERATED TESTS - Django Test Enforcer
# Generated on: 2026-02-13 17:54:03
# These tests FAIL by default - implement them to make them pass!
# ======================================================================


from django.urls import reverse

class TestCrudDjangoFormFunctionViews(TestCase):
    """Auto-generated tests for crud_django_form function-based views - IMPLEMENT THESE!"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.user.is_active = True
        self.user.save()
        self.client.force_login(self.user)

    def test_home_views(self):
        """
        Test home_views
        URL: /crud_django_form/home-views/
        Pattern: custom
        Methods: GET, POST
        Auth Required: No
        
        TODO: Implement this test!
        """
        # TODO: Add test implementation
        # response = self.client.get(reverse("url_name"))
        # self.assertEqual(response.status_code, 200)
        # This test FAILS until you implement it!
        self.fail("TODO: Implement test for home_views")


class TestCrudDjangoFormFunctions(TestCase):
    """Auto-generated tests for crud_django_form functions - IMPLEMENT THESE!"""

    def test_home_views(self):
        """
        Test crud_django_form.urls.home_views
        
        
        TODO: Implement this test!
        """
        # from crud_django_form.urls import home_views
        # result = home_views()
        # self.assertIsNotNone(result)
        
        # This test FAILS until you implement it!
        self.fail("TODO: Implement test for home_views")

    def test_home_views(self):
        """
        Test crud_django_form.views.home_views
        
        
        TODO: Implement this test!
        """
        # from crud_django_form.views import home_views
        # result = home_views()
        # self.assertIsNotNone(result)
        
        # This test FAILS until you implement it!
        self.fail("TODO: Implement test for home_views")

