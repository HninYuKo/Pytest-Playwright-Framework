from playwright.sync_api import Page, expect


def test_simple_alertdialog1(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # Approach 1
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(3000)

    page.locator("#alertBtn").click() #clicking on the button which will open dialog
    page.wait_for_timeout(3000)

def test_simple_alertdialog2(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    #Approach 2
    page.on("dialog",lambda dialog:dialog.accept()) # var=lambda parameters: expressions
    page.wait_for_timeout(3000)

    page.locator("#alertBtn").click()
    page.wait_for_timeout(3000)


def test_confirmation_dialog(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # page.on("dialog",lambda dialog:dialog.accept())
    page.on("dialog",lambda dialog:dialog.dismiss())

    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()
    page.wait_for_timeout(3000)

    text=page.locator("#demo").inner_text()
    print("output text :: ",text)

    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

    page.wait_for_timeout(3000)


def test_prompt_dialog(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    page.on("dialog",lambda dialog:dialog.accept("John Doe"))

    page.wait_for_timeout(3000)

    page.locator("#promptBtn").click()
    page.wait_for_timeout(3000)

    text=page.locator("#demo").inner_text()
    print("output text :: ",text)

    expect(page.locator("#demo")).to_contain_text("John Doe")
    # expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

    page.wait_for_timeout(3000)


