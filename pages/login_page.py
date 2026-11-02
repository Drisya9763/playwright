#Page Object Model solves this problem by seperating page interactions
#from test cases.

#Seperate class:
#Locators -> Identify elements
#methods -> Perform actions such as entering credentials,
#clicking login

#Login_page.py() - Stores login-page locators and methods
from playwright.sync_api import Page 
class LoginPage:
    def __init__(self, page: Page):
        self.page = page 
        #Locators
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')
    #Open the login page
    def open(self) -> None:
        self.page.goto("https://www.saucedemo.com/")
    #Enter username
    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)
    #Enter password        
    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)
    #Click login button
    def click_login(self) -> None:
        self.login_button.click()
    #Perform the complete login operation
    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()