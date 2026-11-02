from pathlib import Path
from playwright.sync_api import expect
def test_payment_iframe(page):
    #Step 1: Open the checkout page
    html_file = Path(__file__).with_name("checkout.html")
    page.goto(html_file.resolve().as_uri())
    #Step 2: Verify main checkout page
    expect(
        page.get_by_role("heading", name="Checkout")
    ).to_be_visible()
    #Step 3: Locate the ifraame and enter it
    payment_frame = page.frame_locator("#payment-frame")
    #Step 4: Locate the cardholder name
    cardholder_name = payment_frame.locator("#card-name")
    cardholder_name.fill("Sachin")
    card_number = payment_frame.locator("#card-number")
    card_number.fill("444411112222")
    page.wait_for_timeout(5000)
    #Step 5: Verify the entered values
    expect(cardholder_name).to_have_value("Sachin")
    expect(card_number).to_have_value("444411112222")
    #Step 6: Click the payment button inside the iframe
    payment_frame.get_by_role(
        "button", name="Pay Now"
    ).click()
    page.wait_for_timeout(5000)
    #Step 7: Verify the success message inside iframe
    expect(
        payment_frame.get_by_role("status")
    ).to_have_text("Payment form submitted successfully.")
    print("Iframe test passed successfully.")

#Playwright Debugging and Reporting 

#Debugging - Helps us to identify and fix this problems
#Reporting - It helps us understand and communicate
#the result of our tests 

#Several Tools to avoid this problems

#1. Codegen - Records browser actions and generates 
#automation code.

#Login Page:
#Inspect the username field
#Find it's locator
#Inspect the password field
#Find it's locatir
#Find the login button
#Write the automation code 