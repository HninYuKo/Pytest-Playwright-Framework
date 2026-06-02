import pytest
from playwright.sync_api import expect

from conftest import page_instance

@pytest.mark.skip
def test_tabs_popup(browser_instance) -> None:
    context=browser_instance.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    #register an event for tab
    page.on("page",lambda page:page.wait_for_load_state())


    page.locator("button:has-text('New Tab')").click()
    page.wait_for_timeout(5000)

    allpages=context.pages

    print(f"number of allpages: {len(allpages)}")

    for page in allpages:
        print(f"page url: {page.url}")
        print(f"page title: {page.title}")


    childpage=allpages[1]
    print(f"child page url: {childpage.url}")
    print(f"child page title: {childpage.title}")

    page.wait_for_timeout(2000)


def test_handle_popup(browser_instance) -> None:
    context=browser_instance.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    #register an event for popup
    page.on("popup",lambda page:page.wait_for_load_state())

    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)

    allpopups=context.pages
    print(f"number of allpopups: {len(allpopups)}")

    for popup in allpopups:

        print(f"popup url: {popup.url}")
        title=popup.title()
        if "Playwright" in title:
            popup.locator(".getStarted_Sjon").click()
            popup.wait_for_timeout(3000)
            expect(popup).to_have_title("Installation | Playwright")
            popup.close()

    page.wait_for_timeout(2000)
    context.close()
    # browser_instance.close()






