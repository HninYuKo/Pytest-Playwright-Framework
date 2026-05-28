import re
from playwright.sync_api import Page, expect


def test_day4_codegen(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    page.wait_for_timeout(3000)
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()

    expect(page.locator("[data-test='shopping-cart-link']")).to_be_visible()
    page.locator("[data-test='shopping-cart-link']").click()
    expect(page.locator("[data-test='item-4-title-link']")).to_be_visible()
    page.wait_for_timeout(2000)
    page.locator("[data-test='item-0-title-link']").click()
    page.wait_for_timeout(1000)
    page.locator("[data-test='remove']").click()
    page.wait_for_timeout(1000)
    page.locator("[data-test='back-to-products']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='back-to-products']")).not_to_be_visible()
