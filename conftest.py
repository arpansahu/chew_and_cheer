"""
Shared Playwright test fixtures and configuration for Django Test Enforcer

UI tests run against a LIVE Django server (not the test database).
Ensure the Django server is running on the configured BASE_URL port.
For authenticated tests, ensure a test user exists in the database.
"""
import pytest
import os
from playwright.sync_api import Page, expect


# Test configuration - Update this to match your local server
# Can be overridden with BASE_URL environment variable
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")


@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for tests"""
    return BASE_URL


@pytest.fixture(scope="session")
def test_user_credentials():
    """
    Test user credentials for authenticated tests.
    
    IMPORTANT: Create this user in your database before running authenticated tests:
        python manage.py shell
        >>> from django.contrib.auth import get_user_model
        >>> User = get_user_model()
        >>> user = User.objects.create_user(email='testuser@example.com', username='testuser', password='TestPass123!')
        >>> user.is_active = True
        >>> user.save()
    """
    return {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "TestPass123!"
    }


@pytest.fixture
def authenticated_page(page: Page, test_user_credentials, base_url):
    """Login and return authenticated page"""
    # Navigate to login page (correct URL: /accounts/login/)
    page.goto(f"{base_url}/accounts/login/", wait_until="domcontentloaded")
    
    # Wait a bit for any redirects or dynamic content
    page.wait_for_timeout(1000)
    
    # Check if we're actually on the login page (not already authenticated)
    current_url = page.url
    if "/login" not in current_url:
        # Already authenticated or redirected
        return page
    
    # Wait for page to be fully loaded
    page.wait_for_load_state("networkidle", timeout=10000)
    
    # Fill login form
    try:
        page.locator("input[name='username']").fill(test_user_credentials["username"])
        page.locator("input[name='password']").fill(test_user_credentials["password"])
        
        # Click the submit button
        page.locator("button[type='submit']").click()
        
        # Wait for navigation after login
        page.wait_for_load_state("networkidle", timeout=10000)
        
    except Exception as e:
        pytest.skip(f"Login failed: {e}")
    
    # Verify login succeeded (should not be on login page anymore)
    if "/login" in page.url:
        # Check for error messages
        error_visible = page.locator(".alert-danger, .errorlist, .error").count() > 0
        if error_visible:
            pytest.skip("Login failed - check test user credentials")
    
    return page
