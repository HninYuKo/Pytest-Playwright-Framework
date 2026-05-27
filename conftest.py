
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page: Page):
    # Pass the Playwright page instance into our custom Page Object
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page):
    # Pass the Playwright page instance into our custom Page Object
    return InventoryPage(page)
