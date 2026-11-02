#Text Extraction

#inner_text() - Returns the rendered text of an element

def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h1").inner_text()
    print(heading)
    assert heading == "Welcome to the-internet"

#text_content() - Returns the text content of a DOM element,including text that may
#not be visible

def test_extract_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading = page.locator("h2").text_content()
    print(heading)
#Using expect() for URL 
from playwright.sync_api import expect 

def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    heading =  page.locator("h1")
    expect(heading).to_have_text("Welcome to the-internet")