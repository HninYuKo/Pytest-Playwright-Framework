from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Define locators using resilient locators
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(3000)

    # Use helper to perform the common "navigate + login + assert inventory url" steps
    def ensure_logged_in(self,username: str = "standard_user", password: str = "secret_sauce"):
        self.navigate()
        self.login(username, password)
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")