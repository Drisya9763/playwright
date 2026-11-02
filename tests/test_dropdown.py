from playwright.sync_api import expect
def test_native_dropdown(page):
    #Step 1: Open URL
    page.goto("https://practice.expandtesting.com/dropdown")
    #Step 2: Locate the simple dropdown
    dropdown = page.locator("#dropdown")
    #Step 3: Verify the dropdown is visible or not 
    expect(dropdown).to_be_visible()
    #Step 4: Select option using it's value
    dropdown.select_option("1")
    #Step 5: Verify selected value
    expect(dropdown).to_have_value("1")
    #Step 6: Select another option
    dropdown.select_option("2")
    #Step 7: Verify new selected value
    expect(dropdown).to_have_value("2")
    print("Dropdown options were selected successfully")
