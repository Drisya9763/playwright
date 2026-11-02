#Handling a New Tab Opened by Clicking a Link

#Open the original website
#Click the link
#Capture the new tab
#Verify the new page
#Interact with the new page

from pathlib import Path
from playwright.sync_api import expect
def test_new_tab_from_link(page):
    #Step 1: Open the local HTML page
    html_file = Path(__file__).with_name("open_new_tab.html")
    page.goto(html_file.resolve().as_uri())
    #Step 2: Verify the original page
    expect(
        page.get_by_role("heading", name="Original Page")
    ).to_be_visible()
    #Step 3: Verify the link exists
    link = page.get_by_role("link", name="Open Example Website in a New Tab")
    expect(link).to_be_visible()
    #Step 4: Click the link and capture new tab
    with page.context.expect_page() as new_page_info:
        link.click()
    new_page = new_page_info.value
    #Step 5:Wait for new tab to finish loading
    new_page.wait_for_load_state("domcontentloaded")
    #Step 6: Verify the new tab URL:
    expect(new_page).to_have_url("https://example.com/")
    print("Oringinal tab URL:", page.url)
    print("New tab URL:", new_page.url)
    #Step 7: Close the new tab
    new_page.close()
    print("New Tab test passed successfully.")