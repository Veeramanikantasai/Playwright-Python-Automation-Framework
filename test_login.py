
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # Open the login page
    page.goto("https://www.saucedemo.com/")

    # Enter username and password
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # Click the login button
    page.locator("#login-button").click()

    # Verify successful login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

def test_invalid_login(page: Page):
    # Open SauceDemo
    page.goto("https://www.saucedemo.com/")

    # Enter incorrect credentials
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")

    # Click Login
    page.locator("#login-button").click()

    # Verify the error message
    error = page.locator('[data-test="error"]')

    expect(error).to_be_visible()
    expect(error).to_contain_text(
        "Username and password do not match"
    )
