
'''
tag id                  tag#id
tag class               tag.class
tag attribute           tag[attribute=value]
tag class attribute     tag.class[attribute=value]

**tag is optional.**
'''

from playwright.sync_api import Page


def test_day2(page: Page):

    page.goto("https://demowebshop.tricentis.com/login")

    #tag id
    page.locator("input#small-searchterms").fill("T-Shirt")
    page.locator("#small-searchterms").fill("T-Shirt")
    page.wait_for_timeout(5000)

    #tag class
    # page.locator("input.search-box-text").fill("T-Shirt")
    # page.locator(".search-box-text").fill("T-Shirt")
    # page.wait_for_timeout(5000)

    #tag attribute
    # page.locator("input[name=q]").fill("Short pants")
    # page.locator("[name=q]").fill("Short pants")
    # page.wait_for_timeout(5000)

    #tag class attribute
    # page.locator("input.search-box-text[value='Search store']").fill("iphone 17 pro")
    # page.locator(".search-box-text[value='Search store']").fill("iphone 17 pro")
    # page.wait_for_timeout(5000)