from playwright.sync_api import Page, expect

def test_multiple_tabs(page: Page):
    #step 1: open first website
    page.goto("https://example.com")
    #Verify the first webpage
    expect(page).to_have_title("Example Domain")
    print("First tab URL: ", page.url)
    #Step 2: Create a second tab in same browser
    second_page = page.context.new_page()
    second_page.goto("https://www.wikipedia.org")
    #Verify the second website
    expect(second_page).to_have_title("Wikipedia")
    print("Second tab URL:", second_page.url)
    #Step 3: Verify the original tab is still open 
    expect(page).to_have_title("Example Domain")
    #Step 4: Verify that two pages exist in the context
    all_pages = page.context.pages
    assert len(all_pages) == 2
    print("No.of open pages:", len(all_pages))
    #Step 5: Interact with the second tab
    expect(
        second_page.get_by_role("heading", name="Wikipedia")
    ).to_be_visible()
    #Step 6: Close the second tab
    second_page.close()
    #Step 7: Verify the original tab remains open
    expect(page).to_have_title("Example Domain")
    assert len(page.context.pages) == 1
    print("Multiple-tabs test passed successfully.")
