import re

from playwright.sync_api import Page, expect


def test_static_table(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)

    table=page.locator("table[name='BookTable'] tbody")

    rows=table.locator("tr")
    # print(f"rows of count::{rows.count()}")
    expect(rows).to_have_count(7)

    cols=rows.locator("th")
    # print(f"cols of count::{cols.count()}")
    expect(cols).to_have_count(4)

    first_row_cells=rows.nth(1).locator("td")
    first_row_text=first_row_cells.all_inner_texts()
    # print(f"first row texts ::{first_row_text}")
    expect(first_row_cells).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    all_row_data=rows.all()
    total_price=0
    # read all rows and cols data
    # print(f"all rows data ::{all_row_data}")
    for row in all_row_data[1:]:
        row_data_list=row.locator("td").all_inner_texts()
        print(f"row_data_list={row_data_list}")

    for row in all_row_data[1:]:
        author_name=row.locator("td").nth(1).inner_text()
        if author_name=="Mukesh":
            book_name=row.locator("td").nth(0).inner_text()
            print(f"author_name={author_name} and book_name = {book_name}")
        col_price=row.locator("td").nth(3).inner_text()
        total_price=total_price+int(col_price)

    print(f"total_price :: {total_price}")



def test_dynamic_table(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)
    #locating the table
    table=page.locator("table[id='taskTable'] tbody")

    #get all rows from the table
    rows=table.locator("tr").all()
    cpu_load=""
    for row in rows:
        process_name=row.locator("td").nth(0).inner_text()
        if process_name=="Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print(f"cpu_load of Chrome= {cpu_load}")

    expect(page.locator(".chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(3000)

def test_pagination_table(page: Page) -> None:

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    page.wait_for_timeout(3000)

    has_more_pages=True
    total_rows=0
    while has_more_pages:
        rows=page.locator("#example tbody tr").all()
        total_rows=total_rows+len(rows)
        for row in rows:
            print(row.inner_text())

        page.wait_for_timeout(3000)
        next_button=page.locator("button[aria-label='Next']")
        is_disabled=next_button.get_attribute("class")

        if "disabled" in is_disabled:
            has_more_pages=False
        else:
            next_button.click()

    print(f"total_rows={total_rows}")

def test_filterrow_pagination_table(page: Page) -> None:

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    page.wait_for_timeout(3000)

    dropdown=page.locator("#dt-length-0")
    dropdown.select_option(label="25")
    page.wait_for_timeout(3000)
    rows=page.locator("#example tbody tr")
    print(f"rows of count={rows.count()}")
    expect(rows).to_have_count(25) #list[locator]can't insert inside expect function

    # page.locator("td",has_text=re.compile("MB$"))