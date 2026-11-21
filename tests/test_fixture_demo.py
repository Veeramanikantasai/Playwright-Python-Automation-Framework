
from playwright.sync_api import Page, expect


def test_inventory_page_after_login(logged_in_page: Page):
    page = logged_in_page

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.locator(".title")
    ).to_have_text("Products")
