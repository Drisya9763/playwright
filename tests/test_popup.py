from pathlib import Path
from playwright.sync_api import expect 

def test_popup_window(page):
    #Step 1: Open the local popup practice html code
    html_file = Path(__file__).with_name("popup_practice.html")
    page.goto(html_file.resolve().as_uri())
    #Step 2: Verify the original page
    expect(
        page.get_by_role(
            "heading", name="Popup Window Practice"
        )
    ).to_be_visible()
    #Step 3: Regsiter popup expectation before clicking 
    with page.expect_popup() as popup_info:
        page.get_by_role(
            "button", name="Open Popup"
        ).click()

    #Step 4: Capture the Popup page
    popup = popup_info.value

    #Step 5: Wait for popup page to load 
    popup.wait_for_load_state("domcontentloaded")

    # #Step 6: Verify the popup URL
    expect(popup).to_have_url("https://example.com/")

    #Step 7: Verify paragraph
    expect(
        popup.locator("p").first
    ).to_contain_text("This domain is for use in documentation examples")

    #Step 8: Verify the Learn more link
    expect(
        popup.get_by_role("link", name="Learn more")
    ).to_be_visible()
    print("Popup test passed successfully")

# iframe - It is a HTML element that embeds another document inside the webpage

#Retries - Running a failed test again automatically.

#First attempt -> Failed
#second Attempt -> Passed



# def test_username_input(page):
#     page.goto("https://www.playwrightautomation.com/practice.html")
#     name_input = page.get_by_placeholder("Enter your name")
#     name_input.fill("Vikas")
#     expect(name_input).to_have_value("Vikas")

#CI-CD pipeline
#Continuous Integrity and Continuous Depolyment or Delivery

#With CI/CD:

#Developer Changes Code -> Developer pushes code to github ->
#GitHub actions starts automatically -> Install python dependencies
#Install Playwright browsers -> Run Playwright tests ->
#generate test reports -> Upload report and debugging artifacts 
#Team reviews the results