
from playwright.sync_api import Page, expect

def test_drag_and_drop(page: Page) -> None:
    # page.goto("https://demo.guru99.com/test/drag_drop.html")

    # Wait until the page is fully loaded (network idle) good for heavy pages
    page.goto("https://demo.guru99.com/test/drag_drop.html", wait_until="networkidle",timeout=40000)
    
    # page.goto("https://demo.guru99.com/test/drag_drop.html", wait_until="domcontentloaded")

    # page.wait_for_selector("#credit2 a")  # BANK block ready
