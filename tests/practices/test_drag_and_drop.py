
from playwright.sync_api import Page, expect

def test_drag_and_drop(page: Page) -> None:
    # page.goto("https://demo.guru99.com/test/drag_drop.html")
    # Wait until the page is fully loaded (network idle) good for heavy pages
    page.goto("https://demo.guru99.com/test/drag_drop.html", wait_until="networkidle",timeout=40000)
    # page.goto("https://demo.guru99.com/test/drag_drop.html", wait_until="domcontentloaded")
    # page.wait_for_selector("#credit2 a")  # BANK block ready


    # Locate source and target
    source = page.locator("#credit2 a")   # Example: BANK block
    target = page.locator("#bank li")     # Example: Drop area

    # Perform drag and drop
    source.drag_to(target)
    page.wait_for_timeout(2000)

    # Locate source and target
    source = page.locator("#credit1 a")   # Example: Sales block
    target = page.locator("#loan li")     # Example: Drop area

    # Perform drag and drop
    source.drag_to(target)
    page.wait_for_timeout(2000)

    # Locate source and target
    source = page.locator("//section[@id='g-container-main']//li[2]")   # Example: 5000 block
    target = page.locator("#amt7 li")     # Example: Drop area

    # Perform drag and drop
    source.drag_to(target)
    page.wait_for_timeout(2000)

    # Locate source and target
    source = page.locator("//section[@id='g-container-main']//li[2]")   # Example: 5000 block
    target = page.locator("#amt8 li")     # Example: Drop area

    # Perform drag and drop
    source.drag_to(target)
    page.wait_for_timeout(2000)

    expect(page.get_by_text("Perfect!")).to_be_visible()

