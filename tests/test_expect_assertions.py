#Expect assertions in Playwright
from playwright.sync_api import expect

def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()