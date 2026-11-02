# from playwright.sync_api import sync_playwright, expect

# def test_login() -> None:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com/")
#         page.locator("[data-test=\"username\"]").fill("standard_user")
#         page.locator("[data-test=\"password\"]").fill("secret_sauce")
#         page.locator("[data-test=\"login-button\"]").click()
#         expect(page).to_have_url("https://www.saucedemo.com/inv")
#         browser.close()


from playwright.sync_api import sync_playwright, expect


from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    # expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#Inspector - It is an interactive debugging tool that lets you inspect and control a 
#playwright test while it runs.

#TraceViewer - It is a debugging tool that lets you
#inspect a recorded test execution afte the test has
#been finished.

#End to end Testing in Playwright Python

#Reusable Functions - Write code once and use it across multiple
#tests

#Test data - Use different inputs to test the same workflow 
#API Mocking - Simulate API responses without calling actual 
#backend service

#End to End Workflow 

#A workflow is a sequence of actions that a user performs to 
#accomplish a task.

#Start ->Open LOgin Page -> Enter Username -> Enter Password ->
# Click Login -> Verify Dashboard -> End 





