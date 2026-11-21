
from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.backpack_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

        self.cart_badge = page.locator(
            ".shopping_cart_badge"
        )

        self.cart_link = page.locator(
            ".shopping_cart_link"
        )

    def add_backpack(self):
        self.backpack_button.click()

    def verify_cart_count(self, count):
        expect(self.cart_badge).to_have_text(str(count))

    def open_cart(self):
        self.cart_link.click()

