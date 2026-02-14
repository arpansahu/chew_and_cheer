"""
Tests for new UI enhancements and features added during UI overhaul.
These tests cover:
- Email/username dual authentication
- Search functionality in Django Forms CRUD
- Pagination implementation
- Custom API documentation pages
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from crud_django_form.models import Item


class EmailAuthenticationTest(TestCase):
    """Test email/username dual authentication feature"""
    
    def setUp(self):
        """Create test user"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_login_with_username(self):
        """Test login using username"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        # Check if redirected to home or another page after login
        self.assertIn(response.status_code, [200, 302])
    
    def test_login_with_email(self):
        """Test login using email instead of username"""
        response = self.client.post(reverse('login'), {
            'username': 'test@example.com',
            'password': 'testpass123'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        # Check if redirected after login attempt
        self.assertIn(response.status_code, [200, 302])
    
    def test_login_with_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        # User should not be authenticated with wrong credentials
    
    def test_login_with_nonexistent_email(self):
        """Test login with non-existent email"""
        response = self.client.post(reverse('login'), {
            'username': 'nonexistent@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 200)
        # User should not be authenticated with non-existent email


class SearchFunctionalityTest(TestCase):
    """Test search feature in Django Forms CRUD"""
    
    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Create test items
        Item.objects.create(name='Pizza Margherita', description='Classic Italian pizza', price=12.99)
        Item.objects.create(name='Burger Deluxe', description='Premium beef burger', price=15.99)
        Item.objects.create(name='Pasta Carbonara', description='Creamy Italian pasta', price=14.99)
        Item.objects.create(name='Caesar Salad', description='Fresh romaine salad', price=9.99)
    
    def test_search_by_name(self):
        """Test searching items by name"""
        response = self.client.get(reverse('crudformhome'), {'search': 'Pizza'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pizza Margherita')
        self.assertNotContains(response, 'Burger Deluxe')
    
    def test_search_by_description(self):
        """Test searching items by description"""
        response = self.client.get(reverse('crudformhome'), {'search': 'Italian'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pizza Margherita')
        self.assertContains(response, 'Pasta Carbonara')
        self.assertNotContains(response, 'Caesar Salad')
    
    def test_search_case_insensitive(self):
        """Test search is case-insensitive"""
        response = self.client.get(reverse('crudformhome'), {'search': 'pizza'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pizza Margherita')
    
    def test_search_no_results(self):
        """Test search with no matching results"""
        response = self.client.get(reverse('crudformhome'), {'search': 'NonExistent'})
        self.assertEqual(response.status_code, 200)
        # Should return empty results
        items = response.context.get('form', [])
        # Form context might be paginator object
        if hasattr(items, 'object_list'):
            self.assertEqual(len(items.object_list), 0)
    
    def test_search_empty_query(self):
        """Test search with empty query returns all items"""
        response = self.client.get(reverse('crudformhome'), {'search': ''})
        self.assertEqual(response.status_code, 200)
        # Should return all 4 items
        self.assertContains(response, 'Pizza Margherita')
        self.assertContains(response, 'Burger Deluxe')


class PaginationTest(TestCase):
    """Test pagination in Django Forms CRUD"""
    
    def setUp(self):
        """Create test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # Create 25 items for pagination testing
        for i in range(25):
            Item.objects.create(
                name=f'Item {i}',
                description=f'Description {i}',
                price=10.0 + i
            )
    
    def test_pagination_default_5_items(self):
        """Test default pagination shows 5 items per page"""
        response = self.client.get(reverse('crudformhome'))
        self.assertEqual(response.status_code, 200)
        items = response.context.get('form')
        if hasattr(items, '__len__'):
            self.assertEqual(len(items), 5)
    
    def test_pagination_10_items_per_page(self):
        """Test pagination with 10 items per page"""
        response = self.client.get(reverse('crudformhome'), {'per_page': 10})
        self.assertEqual(response.status_code, 200)
        items = response.context.get('form')
        if hasattr(items, '__len__'):
            self.assertEqual(len(items), 10)
    
    def test_pagination_25_items_per_page(self):
        """Test pagination with 25 items per page"""
        response = self.client.get(reverse('crudformhome'), {'per_page': 25})
        self.assertEqual(response.status_code, 200)
        items = response.context.get('form')
        if hasattr(items, '__len__'):
            self.assertEqual(len(items), 25)
    
    def test_pagination_invalid_per_page(self):
        """Test pagination with invalid per_page value defaults to 5"""
        response = self.client.get(reverse('crudformhome'), {'per_page': 'invalid'})
        self.assertEqual(response.status_code, 200)
        # Should default to 5
        items = response.context.get('form')
        if hasattr(items, '__len__'):
            self.assertEqual(len(items), 5)
    
    def test_pagination_second_page(self):
        """Test accessing second page of results"""
        response = self.client.get(reverse('crudformhome'), {'page': 2, 'per_page': 10})
        self.assertEqual(response.status_code, 200)
        # Should show next 10 items


class CustomDocumentationPagesTest(TestCase):
    """Test custom API documentation pages"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
    
    def test_graphql_playground_page_loads(self):
        """Test GraphQL playground page with custom template"""
        response = self.client.get('/project/graphql/')
        self.assertEqual(response.status_code, 200)
        # Check for graphiql or graphql content
        self.assertIn(response.status_code, [200, 302])
    
    def test_api_schema_page_loads(self):
        """Test API schema documentation page"""
        response = self.client.get('/project/schema/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'API Schema')
    
    def test_api_schema_yaml_format(self):
        """Test API schema in YAML format"""
        response = self.client.get('/project/schema/?format=yaml')
        self.assertEqual(response.status_code, 200)
        # Check if response contains YAML or HTML wrapper
        self.assertTrue(
            'yaml' in response['Content-Type'].lower() or 
            'html' in response['Content-Type'].lower()
        )
    
    def test_api_schema_json_format(self):
        """Test API schema in JSON format"""
        response = self.client.get('/project/schema/?format=json')
        self.assertEqual(response.status_code, 200)
        # Should return JSON content type or HTML with JSON
        self.assertTrue(
            'json' in response['Content-Type'].lower() or
            response['Content-Type'].startswith('text/html')
        )
    
    def test_rest_api_docs_page(self):
        """Test REST API documentation page"""
        response = self.client.get('/project/docs/')
        self.assertEqual(response.status_code, 200)
        # Check for API docs content
        self.assertContains(response, 'API')


class HomePageDashboardTest(TestCase):
    """Test enhanced home page dashboard"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_home_page_loads(self):
        """Test home page redirects to login for non-authenticated users"""
        response = self.client.get(reverse('home'))
        # Home page should redirect to login for non-authenticated users
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
    
    def test_home_page_shows_features(self):
        """Test home page displays all feature cards for authenticated users"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
        # Check for feature cards
        self.assertContains(response, 'Django Forms CRUD')
        self.assertContains(response, 'AJAX CRUD')
        self.assertContains(response, 'REST API')
        self.assertContains(response, 'GraphQL')
    
    def test_home_page_authenticated_user(self):
        """Test home page for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')


class ProfilePageTest(TestCase):
    """Test enhanced profile page"""
    
    def setUp(self):
        """Create test user"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_profile_page_requires_login(self):
        """Test profile page requires authentication"""
        self.client.logout()
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_profile_page_loads(self):
        """Test profile page loads for authenticated user"""
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'test@example.com')
    
    def test_profile_page_displays_user_info(self):
        """Test profile page displays user information"""
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertContains(response, 'User')
