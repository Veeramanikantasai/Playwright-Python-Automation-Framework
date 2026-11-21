
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login_using_pom(page: Page):

    # Create LoginPage object
    login_page = LoginPage(page)

    # Open website
    login_page.open()

    # Enter login details
    login_page.login("standard_user", "secret_sauce")

    # Verify successful login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
