import pytest
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage

@pytest.fixture(autouse=True)
def login(page):
    LoginPage(page).login("standard_user", "secret_sauce")

def test_inventory_page_loads(page):
    """Inventory page should display 6 products."""
    inventory = InventoryPage(page)
    assert inventory.get_item_count() == 6

def test_add_item_to_cart(page):
    """Adding an item should update cart badge to 1."""
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"

def test_sort_by_name_az(page):
    """Products sorted A-Z should start with 'Sauce Labs Backpack'."""
    inventory = InventoryPage(page)
    inventory.sort_by("az")
    names = inventory.get_all_product_names()
    assert names == sorted(names)

def test_sort_by_name_za(page):
    """Products sorted Z-A should be in descending order."""
    inventory = InventoryPage(page)
    inventory.sort_by("za")
    names = inventory.get_all_product_names()
    assert names == sorted(names, reverse=True)
