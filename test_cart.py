
from playwright.sync_api import Page, expect

def test_add_product_to_cart(page: Page):

    # Open SauceDemo
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Verify login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Add backpack to cart
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # Verify cart quantity
    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")

    # Open cart
    page.locator(".shopping_cart_link").click()

    # Verify backpack is in cart
    expect(
        page.locator(".inventory_item_name")
    ).to_have_text("Sauce Labs Backpack")
