from playwright.sync_api import Page, expect
def test_checkboxes(page: Page):
    #Step 1: Open the page
    page.goto("https://practice.expandtesting.com/checkboxes")
    #Step 2: Locate the first and second checkboxes 
    checkboxes = page.locator('input[type="checkbox"]')
    first_checkbox = checkboxes.nth(0) #Checkbox 1
    second_checkbox = checkboxes.nth(1) #Checkbox 2
    #Step 3: Verify that both checkboxes are visible or not
    expect(first_checkbox).to_be_visible()
    expect(second_checkbox).to_be_visible()
    #Step 4: Select the first checkbox
    first_checkbox.check()
    #Step 5: Verify that first checkbox is selected
    expect(first_checkbox).to_be_checked()
    #Step 6: Verify the second checkbox is checked
    expect(second_checkbox).to_be_checked()
    #Step 7: Deselect the first checkbox 
    first_checkbox.uncheck()
    #Step 8: Verify the final states
    expect(first_checkbox).not_to_be_checked()
    expect(second_checkbox).to_be_checked()
    print("Checkbox selection and deselection tests passed")