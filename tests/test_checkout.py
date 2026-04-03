import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage

@pytest.fixture(autouse=True)
def login_and_add_item(page):
    LoginPage(page).login("standard_user", "secret_sauce")
    InventoryPage(page).add_first_item_to_cart()
    page.locator(".shopping_cart_link").click()

def test_cart_has_one_item(page):
    """Cart should contain 1 item after adding."""
    cart = CartPage(page)
    assert cart.get_cart_item_count() == 1

def test_remove_item_from_cart(page):
    """Removing item should empty the cart."""
    cart = CartPage(page)
    cart.remove_first_item()
    assert cart.get_cart_item_count() == 0

def test_checkout_flow(page):
    """Completing checkout should show order confirmation."""
    cart = CartPage(page)
    cart.proceed_to_checkout()
    page.locator("[data-test='firstName']").fill("Abu")
    page.locator("[data-test='lastName']").fill("Afridi")
    page.locator("[data-test='postalCode']").fill("1206")
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
    confirmation = page.locator(".complete-header").text_content()
    assert "Thank you" in confirmation
