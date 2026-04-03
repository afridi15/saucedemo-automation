class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_item_count(self):
        return self.inventory_items.count()

    def add_first_item_to_cart(self):
        self.page.locator(".btn_primary.btn_inventory").first.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()

    def sort_by(self, option):
        self.sort_dropdown.select_option(option)

    def get_all_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()
