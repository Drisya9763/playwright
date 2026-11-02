import pytest
from playwright.sync_api import Page, expect

from test_data.login_data import LOGIN_TEST_DATA

@pytest.mark.parametrize("test_data", LOGIN_TEST_DATA)
def test_login(page: Page, test_data: dict):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill(test_data["username"])
    page.locator('[data-test="password"]').fill(test_data["password"])
    page.locator('[data-test="login-button"]').click()
    if test_data["expected"] == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator('[data-test="error"]')).to_be_visible()
        