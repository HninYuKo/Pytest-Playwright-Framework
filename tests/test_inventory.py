from playwright.sync_api import Page,expect
import re
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_inventory_addtocart(page_instance) -> None:
    page = page_instance
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1. Navigate to inventory page (via login)
    login_page.ensure_logged_in()
    page.wait_for_timeout(3000)

    inventory_page.add_to_cart()

    # 3. Assertions (Playwright auto-waits for assertions)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.wait_for_timeout(3000)
