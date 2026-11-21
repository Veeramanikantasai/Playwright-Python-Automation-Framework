
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_using_pom(logged_in_page: Page):

    page = logged_in_page

    # Add product to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_backpack()
    inventory_page.verify_cart_count(1)
    inventory_page.open_cart()

    # Verify product
    expect(
        page.locator(".cart_item .inventory_item_name")
    ).to_have_text("Sauce Labs Backpack")

    # Start checkout
    page.locator("#checkout").click()

    # Enter customer details
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_details(
        "Veera", "Sai", "Dublin"
    )

    checkout_page.continue_checkout()
    checkout_page.verify_overview()

    # Complete order
    checkout_page.finish_order()
    checkout_page.verify_order_confirmation()
