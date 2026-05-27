from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Define locators using resilient locators
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-onesie")
        self.add_to_cart_link = page.locator("//a[@class='shopping_cart_link']")

    # def navigate(self):
    #     self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        self.page.wait_for_timeout(2000)
        self.add_to_cart_link.click()

