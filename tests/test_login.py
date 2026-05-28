from playwright.sync_api import Page,expect
from pages.login_page import LoginPage


def test_successful_login(page: Page) -> None:

    login_page = LoginPage(page)

    # 1. Navigate to login
    login_page.navigate()

    # 2. Perform actions using POM methods
    login_page.login("standard_user", "secret_sauce")

    # 3. Assertions (Playwright auto-waits for assertions)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.wait_for_timeout(5000)