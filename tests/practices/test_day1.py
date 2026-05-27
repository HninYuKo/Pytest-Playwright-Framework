import re
from playwright.sync_api import Page, expect

def test_day1(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    page.get_by_label("Email Address:").fill("hninyuko@gmail.com")
    page.get_by_label("Password:").fill("abcdefghijklmnop")
    page.get_by_label("Your Age:").fill("34")
    page.get_by_label("Standard").click()
    # rdotxt=page.get_by_label("Express").get_attribute("name")
    # print(f"rdotxt: {rdotxt}")

    page.get_by_placeholder("Enter your full name").fill("Hnin Yu Ko")
    page.get_by_placeholder("Phone number (xxx-xxx-xxxx)").fill("099-765-54436")

    expect(page.get_by_alt_text("logo image")).not_to_be_disabled()
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    expect(page.get_by_title("Click to save your changes")).to_have_text("Save")

    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    # page.wait_for_timeout(3000)
