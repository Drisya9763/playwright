#Example: Click a Button
from playwright.sync_api import expect
def test_click_button(page):
    page.goto("https://www.playwrightautomation.com/practice.html")
    button = page.get_by_role(
        "button", 
        name="Submit"
    )
    expect(button).to_be_visible()
    button.click()
