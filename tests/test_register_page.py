from playwright.sync_api import Page, expect

def test_zoom_meeting_registration(page: Page):
    #Step 1: Open Zoom registration page
    page.goto("https://ust.zoom.us/meeting/register/wROkcnzOSO2Z7jeg-vMTPA#/registration")
    #Step 2: Enter First Name
    page.get_by_label("First Name").fill("Vikas")
    #Step 3: Enter Last Name
    page.get_by_label("Last Name").fill("P")
    #Step 4: Email
    page.get_by_label("Email Address").fill("vikasp@gmail.com")
    #Step 5: Enter UST UID
    page.get_by_label("UST UID").fill("123456")
    #Step 6: Verify the entered info
    expect(page.get_by_label("First Name")).to_have_value("Vikas")
    expect(page.get_by_label("Last Name")).to_have_value("P")
    expect(page.get_by_label("Email Address")).to_have_value("vikasp@gmail.com")
    expect(page.get_by_label("UST UID")).to_have_value("123456")
    #Step 7: Locate the Resigter and Join Button
    register_button = page.get_by_role("button", name="Register and Join")
    #Step 8: Verify the button is visible
    expect(register_button).to_be_visible()
