import pytest
from tests.pages.login_page import LoginPage

VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"

def test_valid_login(page):
    """Standard user should log in successfully."""
    login = LoginPage(page)
    login.login(VALID_USER, PASSWORD)
    assert "/inventory" in page.url

def test_invalid_credentials(page):
    """Wrong password should show error message."""
    login = LoginPage(page)
    login.login("wrong_user", "wrong_pass")
    error = login.get_error_message()
    assert "Username and password do not match" in error

def test_empty_username(page):
    """Empty username should show validation error."""
    login = LoginPage(page)
    login.login("", PASSWORD)
    error = login.get_error_message()
    assert "Username is required" in error

def test_empty_password(page):
    """Empty password should show validation error."""
    login = LoginPage(page)
    login.login(VALID_USER, "")
    error = login.get_error_message()
    assert "Password is required" in error

def test_locked_user(page):
    """Locked user should see specific error message."""
    login = LoginPage(page)
    login.login(LOCKED_USER, PASSWORD)
    error = login.get_error_message()
    assert "locked out" in error
