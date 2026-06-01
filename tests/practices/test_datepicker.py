
from playwright.sync_api import Page, expect

def select_checkin_date(page: Page,year,month,day):

    while True:
        checkin_month_year=page.locator("h3[class='e7addce19e af236b7586']").nth(0).inner_text()
        current_month,current_year=checkin_month_year.split(" ")

        if current_month==month and current_year==year:
            print(f"{current_month} and {current_year}")
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates=page.locator("table[class='b8fcb0c66a'] tbody").nth(0).locator("td").all()

    for date in all_dates:
        if date==day:
            date.click()
            break


def select_checkout_date(page: Page,year,month,day):

    while True:
        checkout_month_year=page.locator("h3[class='e7addce19e af236b7586']").nth(1).inner_text()
        current_month,current_year=checkout_month_year.split(" ")

        if current_month==month and current_year==year:
            print(f"{current_month} and {current_year}")
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates=page.locator("table[class='b8fcb0c66a'] tbody").nth(1).locator("td").all()

    for date in all_dates:
        if date==day:
            date.click()
            break



def test_datepicker_booking(page: Page) -> None:

    page.goto("https://booking.com/")
    page.wait_for_timeout(5000)

    # Listen for dialog events
    page.keyboard.press("Escape")
    # expect(page.locator("div[role='dialog']")).to_be_visible()
    # page.locator("button[aria-label='Dismiss sign in information.']").click()
    page.wait_for_timeout(2000)

    page.get_by_test_id("searchbox-dates-container").click()

    select_checkin_date(page,"2026","June","01")
    select_checkout_date(page, "2026", "June", "15")

    checkin_text=page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text=page.locator("span[data-testid='date-display-field-end']").inner_text()

    print(f"{checkin_text} and {checkout_text}")
    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(3000)
