#Reusable function

#Function that you define once and call whenever you need it's
#functionality 

#Suppose you have this test:

#Test1: Login and View Products
#Test2: Loign and add product to the cart
#Test3: Login and remove a product 

from playwright.sync_api import Page, expect 
def login(page: Page, username: str, password: str) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    page.wait_for_timeout(5000)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
def test_login_and_view_products(page: Page):
    login(page, "standard_user", "secret_sauce")
    page.wait_for_timeout(5000)
    expect(page.locator(".inventory_item")).to_have_count(6)
    page.wait_for_timeout(5000)
def test_login_and_add_product(page: Page):
    login(page, "standard_user", "secret_sauce")
    page.wait_for_timeout(5000)
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.wait_for_timeout(5000)

    