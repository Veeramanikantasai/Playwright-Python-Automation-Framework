
import re
from playwright.sync_api import Page, expect

def test_open_playwright(page: Page):
    # Open the Playwright website
    page.goto("https://playwright.dev/")

    # Verify the website title
    expect(page).to_have_title(re.compile("Playwright"))
