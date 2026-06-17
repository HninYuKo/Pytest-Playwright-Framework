from playwright.sync_api import Page, expect


def test_end_2_end(page_instance) -> None:
    page=page_instance
    page.goto("https://blazedemo.com/")
    page.wait_for_timeout(3000)

    fromPortSelect=page.locator("select[name='fromPort']")
    fromPortSelect.select_option(value="Portland")

    toPortSelect = page.locator("select[name='toPort']")
    toPortSelect.select_option(value="Dublin")

    page.locator("input[type='submit']").click()
    page.wait_for_timeout(2000)
    expect(page).to_have_url("https://blazedemo.com/reserve.php")

    title=page.locator("h3")
    expect(title).to_be_visible()
    expect(title).to_contain_text("Portland to Dublin:")
    page.wait_for_timeout(2000)

    rows=page.locator("tbody tr").all()
    price=[]
    for row in rows:
        price.append(row.locator("td").nth(5).inner_text())

    # print(f"price: {price}")
    sorted_price=sorted(price)
    # print(f"sorted_price: {sorted_price}")
    lowest_price=sorted_price[0]
    # print(f"lowest_price: {lowest_price}")

    for row in rows:
        col_price=row.locator("td").nth(5).inner_text()
        if col_price==lowest_price:
            print(f"col_price {col_price} == lowest_price: {lowest_price}")
            col_choose_btn=row.locator("td").nth(0)
            col_choose_btn.click()
            break

    page.wait_for_timeout(2000)
    expect(page).to_have_url("https://blazedemo.com/purchase.php")

    title = page.locator("h2")
    expect(title).to_be_visible()
    expect(title).to_contain_text("Your flight from TLV to SFO has been reserved.")

    page.locator("input[id='inputName']").fill("John Doe")
    page.locator("input[id='address']").fill("Dublin")
    page.locator("input[id='city']").fill("Portland")
    page.locator("input[id='state']").fill("United States")
    page.locator("input[id='zipCode']").fill("12345")
    page.locator("select[id='cardType']").select_option(value="dinersclub")
    page.wait_for_timeout(2000)
    page.locator("input[id='creditCardNumber']").fill("123456789")
    page.locator("input[id='creditCardMonth']").fill("05")
    page.locator("input[id='creditCardYear']").fill("2030")
    page.locator("input[id='nameOnCard']").fill("John Doe")
    page.locator("input[id='rememberMe']").check()
    page.wait_for_timeout(2000)
    page.locator("input[type='submit']").click()

    page.wait_for_timeout(2000)
    expect(page).to_have_url("https://blazedemo.com/confirmation.php")

    title = page.locator("h1")

    expect(title).to_be_visible()
    expect(title).to_contain_text("Thank you for your purchase today!")


