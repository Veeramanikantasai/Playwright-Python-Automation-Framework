
from playwright.sync_api import Page, expect


def test_complete_checkout(page: Page):

    # Open SauceDemo
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Verify successful login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Add a product to cart
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # Open shopping cart
    page.locator(".shopping_cart_link").click()

    # Verify product in cart
    expect(
        page.locator(".inventory_item_name")
    ).to_have_text("Sauce Labs Backpack")

    # Click Checkout
    page.locator("#checkout").click()

    # Enter customer information
    page.locator("#first-name").fill("Veera")
    page.locator("#last-name").fill("Sai")
    page.locator("#postal-code").fill("Dublin")

    # Continue checkout
    page.locator("#continue").click()

    # Verify checkout overview
    expect(
        page.locator(".title")
    ).to_have_text("Checkout: Overview")

    # Finish order
    page.locator("#finish").click()

    # Verify order confirmation
    expect(
        page.locator(".complete-header")
    ).to_have_text("Thank you for your order!")
