
import re
from playwright.sync_api import Page, expect


def test_day5(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_role("button", name="Primary Action").click()
    page.get_by_role("textbox", name="Username:").fill("hninyuko")
    page.get_by_role("button", name="Submit Form").click()
    expect(page.get_by_text("Locate form controls by their")).to_be_visible()
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="Email Address:").click()
    page.get_by_role("textbox", name="Email Address:").fill("hninyuko@gmail.com")
    page.get_by_role("textbox", name="Password:").fill("abc123")
    page.get_by_role("spinbutton", name="Your Age:").fill("32")
    page.wait_for_timeout(3000)
    page.get_by_role("radio", name="Standard").check()
    expect(page.get_by_role("img", name="logo image")).to_be_visible()
    expect(page.get_by_text("This text has a tooltip")).to_be_visible()
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)


