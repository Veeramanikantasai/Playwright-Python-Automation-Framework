
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage


def test_add_backpack_using_pom(logged_in_page: Page):

    page = logged_in_page

    inventory_page = InventoryPage(page)

    # Add backpack
    inventory_page.add_backpack()

    # Verify cart count
    inventory_page.verify_cart_count(1)

    # Open shopping cart
    inventory_page.open_cart()

    # Verify product
    expect(
        page.locator(".cart_item .inventory_item_name")
    ).to_have_text("Sauce Labs Backpack")
