def test_username(user_data):
    assert user_data["username"] == "testuser"

def test_username():
    username = "admin"
    assert username == "admin"

def test_values():
    assert 10 > 5
    assert "Python" in "Python Playwright"
    assert 5 != 3
    assert [1, 2, 3] == [1, 2, 3]

#Parameterization - Testing Multiple Inputs
#It allows one test function to run with different input 
#values 

import pytest
@pytest.mark.parametrize(
    "number, expected",
    [
        (2, 4),
        (3, 9),
        (4, 16)
    ]
)
def test_square(number, expected):
    assert number * number == expected


#Markers - Organizing tests into categories 

#Smoke test: Quick checks of essential functionality
#Regression tests: Checks that existing functionality still
#work
#Slow tests: Tests that take longer to execute.

import pytest
@pytest.mark.smoke
def test_homepage_title():
    assert "Home" == "Home"
@pytest.mark.regression
def test_user_status():
    assert "Active" == "Active"
    
#Eg: Verify a Username input 

from playwright.sync_api import expect

def test_username_input(page):
    page.goto("https://www.playwrightautomation.com/practice.html")
    name_input = page.get_by_placeholder("Enter your name")
    name_input.fill("Vikas")
    expect(name_input).to_have_value("Vikas")


def test_heading(page):
    page.goto("https://the-internet.herokuapp.com/")
    href = page.get_by_role("link", name="Subdirectories").get_attribute("href")
    print(href)

#Waiting Mechanism in Playwright 


#Explicit wait using locator.wait_for() 
from playwright.sync_api import expect
def test_dynamic_loading(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    heading = page.locator("#finish h4")
    expect(heading).to_have_text("Hello World!")

