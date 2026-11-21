
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Sorry, this user has been locked out."
        ),
        (
            "invalid_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "standard_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "",
            "secret_sauce",
            "Username is required"
        ),
        (
            "standard_user",
            "",
            "Password is required"
        )
    ]
)
def test_invalid_login_data(
    page: Page,
    username,
    password,
    expected_error
):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    expect(
        page.locator('[data-test="error"]')
    ).to_contain_text(expected_error)
