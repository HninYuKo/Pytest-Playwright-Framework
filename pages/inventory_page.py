from playwright.sync_api import Page

from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Define locators using resilient locators
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-onesie")
        self.add_to_cart_link = page.locator("//a[@class='shopping_cart_link']")
        self.add_to_cart_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_to_cart_bike_light = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.add_to_cart_bolt_t_shirt = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.shopping_cart_link=page.locator("[data-test='shopping-cart-link']")
        self.item4_title_link=page.locator("[data-test='item-4-title-link']")
        self.item0_title_link=page.locator("[data-test='item-0-title-link']")
        self.remove=page.locator("[data-test='remove']")
        self.back_to_products=page.locator("[data-test='back-to-products']")

    # def navigate(self):
    #     self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_to_cart(self):
        self.add_to_cart_backpack.click()
        self.add_to_cart_bike_light.click()
        self.add_to_cart_bolt_t_shirt.click()
        expect(self.shopping_cart_link).to_be_visible()
        self.shopping_cart_link.click()
        expect(self.item4_title_link).to_be_visible()
        self.page.wait_for_timeout(2000)
        self.item0_title_link.click()
        self.page.wait_for_timeout(1000)
        self.remove.click()
        self.page.wait_for_timeout(1000)
        self.back_to_products.click()


