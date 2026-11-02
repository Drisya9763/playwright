from playwright.sync_api import expect 

def test_wait_for_url(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/secure")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
