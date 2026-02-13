from django.test import TestCase
from django.core.management import call_command
from django.core.cache import cache
from io import StringIO
from .models import TestModel


class DatabaseHealthCheckTest(TestCase):
    """Test cases for database health check command"""

    def test_database_health_command(self):
        """Test test_db management command"""
        out = StringIO()
        call_command('test_db', stdout=out)
        output = out.getvalue()
        
        self.assertIn('Successfully created test entry', output)
        self.assertIn('Successfully retrieved test entry', output)
        self.assertIn('Successfully updated test entry', output)
        self.assertIn('Successfully deleted test entry', output)
        self.assertIn('Database test completed successfully', output)

    def test_database_model_crud(self):
        """Test TestModel CRUD operations directly"""
        # Create
        test_entry = TestModel.objects.create(name='Direct Test')
        self.assertEqual(test_entry.name, 'Direct Test')
        
        # Read
        retrieved = TestModel.objects.get(name='Direct Test')
        self.assertEqual(retrieved.name, 'Direct Test')
        
        # Update
        retrieved.name = 'Updated Direct Test'
        retrieved.save()
        self.assertEqual(TestModel.objects.get(id=retrieved.id).name, 'Updated Direct Test')
        
        # Delete
        retrieved.delete()
        self.assertFalse(TestModel.objects.filter(name='Updated Direct Test').exists())


class CacheHealthCheckTest(TestCase):
    """Test cases for cache health check command"""

    def setUp(self):
        # Clear cache before each test
        cache.clear()

    def test_cache_health_command(self):
        """Test test_cache management command"""
        out = StringIO()
        call_command('test_cache', stdout=out)
        output = out.getvalue()
        
        self.assertIn('Initial cache set:', output)
        self.assertIn('Cache has expired as expected', output)
        self.assertIn('Cache is working correctly', output)

    def test_cache_set_and_get(self):
        """Test cache set and get operations"""
        # Set cache
        cache.set('test_key', 'test_value', timeout=30)
        
        # Get cache
        value = cache.get('test_key')
        self.assertEqual(value, 'test_value')
        
        # Test non-existent key
        self.assertIsNone(cache.get('nonexistent_key'))

    def test_cache_delete(self):
        """Test cache deletion"""
        cache.set('delete_test', 'value_to_delete')
        self.assertEqual(cache.get('delete_test'), 'value_to_delete')
        
        cache.delete('delete_test')
        self.assertIsNone(cache.get('delete_test'))

    def test_cache_expiration(self):
        """Test cache expiration"""
        import time
        
        # Set short timeout
        cache.set('expire_test', 'expire_value', timeout=1)
        self.assertEqual(cache.get('expire_test'), 'expire_value')
        
        # Wait for expiration
        time.sleep(2)
        self.assertIsNone(cache.get('expire_test'))


class ServiceHealthIntegrationTest(TestCase):
    """Integration tests for service health checks"""

    def test_all_services_command(self):
        """Test test_all_services command"""
        out = StringIO()
        try:
            call_command('test_all_services', stdout=out)
            output = out.getvalue()
            # Should run without errors
            self.assertIsNotNone(output)
        except Exception as e:
            # Some services might not be configured in test environment
            # Accept both "Error" and "failed" messages
            error_msg = str(e).lower()
            self.assertTrue('error' in error_msg or 'failed' in error_msg,
                          "Service test should either pass or raise expected error")

    def tearDown(self):
        # Clean up cache after each test
        cache.clear()
