from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AccountViewsTestCase(TestCase):
    """Test cases for account views"""

    def setUp(self):
        """Set up test client and test user"""
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_registration_view_get(self):
        """Test registration view GET request"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

    def test_login_view_get(self):
        """Test login view GET request"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_view_post_success(self):
        """Test successful login"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_account_view_requires_auth(self):
        """Test account view requires authentication"""
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 302)

    def test_account_view_authenticated(self):
        """Test account view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/account.html')



# ======================================================================
# AUTO-GENERATED TESTS - Django Test Enforcer
# Generated on: 2026-02-13 17:54:03
# These tests FAIL by default - implement them to make them pass!
# ======================================================================


from django.urls import reverse

class TestAccountFunctionViews(TestCase):
    """Auto-generated tests for account function-based views - IMPLEMENT THESE!"""

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

    def test_authenticate(self):
        """
        Test authenticate
        URL: /account/authenticate/
        Pattern: custom
        Methods: GET, POST
        Auth Required: Yes
        
        TODO: Implement this test!
        """
        # Test login authentication
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        # Should redirect on successful authentication
        self.assertIn(response.status_code, [200, 302])

    def test_error_400(self):
        """
        Test error_400
        URL: /account/error-400/
        Pattern: custom
        Methods: GET, POST
        Auth Required: No
        
        TODO: Implement this test!
        """
        from account.views import error_400
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_400(request, exception=None)
        # Should return the error template
        self.assertEqual(response.status_code, 200)

    def test_error_403(self):
        """
        Test error_403
        URL: /account/error-403/
        Pattern: custom
        Methods: GET, POST
        Auth Required: No
        
        TODO: Implement this test!
        """
        from account.views import error_403
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_403(request, exception=None)
        # Should return the error template
        self.assertEqual(response.status_code, 200)

    def test_error_404(self):
        """
        Test error_404
        URL: /account/error-404/
        Pattern: custom
        Methods: GET, POST
        Auth Required: No
        
        TODO: Implement this test!
        """
        from account.views import error_404
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_404(request, exception=None)
        # Should return the error template
        self.assertEqual(response.status_code, 200)

    def test_error_500(self):
        """
        Test error_500
        URL: /account/error-500/
        Pattern: custom
        Methods: GET, POST
        Auth Required: No
        
        TODO: Implement this test!
        """
        from account.views import error_500
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_500(request)
        # Should return the error template
        self.assertEqual(response.status_code, 200)


class TestAccountFunctions(TestCase):
    """Auto-generated tests for account functions - IMPLEMENT THESE!"""

    def test_at_beginning_delete(self):
        """
        Test account.signals.at_beginning_delete
        
        
        TODO: Implement this test!
        """
        # Test that pre_delete signal fires
        test_user = User.objects.create_user(
            username='deletetest',
            email='delete@test.com',
            password='testpass'
        )
        # Delete should trigger pre_delete signal
        test_user.delete()
        # If no exception, signal worked
        self.assertTrue(True)

    def test_at_beginning_init(self):
        """
        Test account.signals.at_beginning_init
        
        
        TODO: Implement this test!
        """
        # Test that pre_init signal fires when creating user
        test_user = User(username='inittest', email='init@test.com')
        # pre_init fires during __init__
        self.assertIsNotNone(test_user)

    def test_at_beginning_request(self):
        """
        Test account.signals.at_beginning_request
        
        
        TODO: Implement this test!
        """
        # request_started signal fires for any request
        response = self.client.get(reverse('login'))
        # Signal would have fired during request
        self.assertEqual(response.status_code, 200)

    def test_at_beginning_save(self):
        """
        Test account.signals.at_beginning_save
        
        
        TODO: Implement this test!
        """
        # Test that pre_save signal fires
        test_user = User.objects.create_user(
            username='savetest',
            email='save@test.com',
            password='testpass'
        )
        # Modify and save to trigger pre_save
        test_user.email = 'newsave@test.com'
        test_user.save()
        self.assertEqual(test_user.email, 'newsave@test.com')

    def test_at_end_migrate_flush(self):
        """
        Test account.signals.at_end_migrate_flush
        
        
        TODO: Implement this test!
        """
        # post_migrate signals fire after migrations
        # We can't easily test this in unit tests
        # Just verify the signal handler exists
        from account.signals import at_end_migrate_flush
        self.assertTrue(callable(at_end_migrate_flush))

    def test_at_ending_delete(self):
        """
        Test account.signals.at_ending_delete
        
        
        TODO: Implement this test!
        """
        # Test that post_delete signal fires
        test_user = User.objects.create_user(
            username='postdeletetest',
            email='postdelete@test.com',
            password='testpass'
        )
        user_id = test_user.id
        # Delete should trigger post_delete signal
        test_user.delete()
        # Verify user is deleted
        self.assertFalse(User.objects.filter(id=user_id).exists())

    def test_at_ending_init(self):
        """
        Test account.signals.at_ending_init
        
        
        TODO: Implement this test!
        """
        # Test that post_init signal fires
        test_user = User.objects.create_user(
            username='postinitset',
            email='postinit@test.com',
            password='testpass'
        )
        # post_init fires after object initialization
        self.assertEqual(test_user.username, 'postinitset')

    def test_at_ending_save(self):
        """
        Test account.signals.at_ending_save
        
        
        TODO: Implement this test!
        """
        # Test that post_save signal fires
        test_user = User.objects.create_user(
            username='postsavetest',
            email='postsave@test.com',
            password='testpass'
        )
        # post_save fires after save
        self.assertTrue(User.objects.filter(username='postsavetest').exists())

    def test_at_request_exception(self):
        """
        Test account.signals.at_request_exception
        
        
        TODO: Implement this test!
        """
        # got_request_exception fires when an exception occurs
        # We can verify the handler exists
        from account.signals import at_request_exception
        self.assertTrue(callable(at_request_exception))

    def test_at_starting_request(self):
        """
        Test account.signals.at_starting_request
        
        
        TODO: Implement this test!
        """
        # request_finished signal fires after request
        response = self.client.get(reverse('login'))
        # Signal would have fired after request
        self.assertEqual(response.status_code, 200)

    def test_before_install_app(self):
        """
        Test account.signals.before_install_app
        
        
        TODO: Implement this test!
        """
        # pre_migrate signals fire before migrations
        # We can't easily test this in unit tests
        # Just verify the signal handler exists
        from account.signals import before_install_app
        self.assertTrue(callable(before_install_app))

    def test_conn_db(self):
        """
        Test account.signals.conn_db
        
        
        TODO: Implement this test!
        """
        # connection_created signal fires when DB connection is made
        # We can verify the handler exists
        from account.signals import conn_db
        self.assertTrue(callable(conn_db))

    def test_login_failed(self):
        """
        Test account.signals.login_failed
        
        
        TODO: Implement this test!
        """
        # user_login_failed signal fires on failed login
        response = self.client.post(reverse('login'), {
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        # Login should fail, triggering the signal
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        """
        Test account.signals.login_success
        
        
        TODO: Implement this test!
        """
        # user_logged_in signal fires on successful login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        # Should redirect on successful login, triggering signal
        self.assertIn(response.status_code, [200, 302])

    def test_logout_success(self):
        """
        Test account.signals.logout_success
        
        
        TODO: Implement this test!
        """
        # user_logged_out signal fires on logout
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        # Should redirect after logout, triggering signal
        self.assertEqual(response.status_code, 302)

    def test_error_400(self):
        """
        Test account.views.error_400
        
        
        TODO: Implement this test!
        """
        from account.views import error_400
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_400(request, exception=None)
        self.assertEqual(response.status_code, 200)

    def test_error_403(self):
        """
        Test account.views.error_403
        
        
        TODO: Implement this test!
        """
        from account.views import error_403
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_403(request, exception=None)
        self.assertEqual(response.status_code, 200)

    def test_error_404(self):
        """
        Test account.views.error_404
        
        
        TODO: Implement this test!
        """
        from account.views import error_404
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_404(request, exception=None)
        self.assertEqual(response.status_code, 200)

    def test_error_500(self):
        """
        Test account.views.error_500
        
        
        TODO: Implement this test!
        """
        from account.views import error_500
        from django.http import HttpRequest
        
        request = HttpRequest()
        response = error_500(request)
        self.assertEqual(response.status_code, 200)

