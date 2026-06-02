
from playwright.sync_api import Page, expect

def select_checkinout_date(page: Page,year,month,day):

    while True:
        checkin_month_year=page.locator("h3[class='e7addce19e af236b7586']").nth(0).inner_text()
        current_month,current_year = checkin_month_year.split(" ")  #june 2026
        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates=page.locator("table[class='b8fcb0c66a'] tbody").nth(0).locator("td").all()

    for date in all_dates:
        txt_date=date.inner_text()
        if txt_date==day:
            date.click()
            break


def test_datepicker_booking(page_instance) -> None:

    page=page_instance
    # page=page_instance
    page.goto("https://booking.com/")
    page.wait_for_timeout(3000)

    page.locator("div[class='b779265b5e'] button").wait_for(state="visible")
    page.locator("div[class='b779265b5e'] button").click()
    page.wait_for_timeout(2000)

    page.get_by_test_id("searchbox-dates-container").click()

    page.wait_for_timeout(2000)
    select_checkinout_date(page,"2026","June","15")
    page.wait_for_timeout(2000)
    select_checkinout_date(page,"2027","January","4")
    page.wait_for_timeout(3000)

    checkin_text=page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text=page.locator("span[data-testid='date-display-field-end']").inner_text()

    print(f"{checkin_text} :: and :: {checkout_text}")
    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(3000)
