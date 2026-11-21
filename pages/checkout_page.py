
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)

    def continue_checkout(self):
        self.page.locator("#continue").click()

    def verify_overview(self):
        expect(
            self.page.locator(".title")
        ).to_have_text("Checkout: Overview")

    def finish_order(self):
        self.page.locator("#finish").click()

    def verify_order_confirmation(self):
        expect(
            self.page.locator(".complete-header")
        ).to_have_text("Thank you for your order!")
