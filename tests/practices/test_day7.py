import re

from playwright.sync_api import Page, expect


def test_hidden_dropdown_bootstrap(page: Page) -> None:

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Recruitment")).to_be_visible()
    # expect(page.get_by_label("Sidepanel").get_by_role("list")).to_contain_text("Leave")
    # expect(page.get_by_label("Sidepanel").get_by_role("list")).to_contain_text("Admin")

    page.get_by_text("PIM").click()
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(3000)
    # job_title_options=page.locator("div.oxd-select-option").all_text_contents()
    # job_title_options=page.locator("div[role='listbox'] span").all_text_contents()

    job_title_options=page.locator("div[role='listbox'] span")
    # print(f"job_title_options count: {job_title_options.count()}")
    expect(job_title_options).to_have_count(job_title_options.count())

    # for i in range(job_title_options.count()):
    #     print(f"job title {i} :: {job_title_options.nth(i).text_content()}")

    for i in range(job_title_options.count()):
        txt_job=job_title_options.nth(i).text_content()
        if(txt_job=="QA Engineer"):
            job_title_options.nth(i).click()
            break

    page.wait_for_timeout(3000)

def test_hidden_dropdown(page: Page) -> None:

    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(5000)

    page.locator("span[role='button']").click()
    page.wait_for_timeout(2000)

    page.locator("//form[@class='lilxh_ header-form-search']//input[@placeholder='Search for Products, Brands and More']").fill("mobile")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(2000)

    expect(page).to_have_url(re.compile(r"flipkart\.com/search/?")) # regex pattern #partial link check
    page.wait_for_timeout(5000)

    page.locator("input[name='q']").click()
    page.wait_for_timeout(2000)

    item_list=page.locator("div[class='pVNZxj KIiP4i']")
    item_txt=item_list.nth(4).inner_text()
    item_list.nth(4).click()
    page.wait_for_timeout(2000)

    search_result=page.locator("span[class='_Omnvo']")
    expect(search_result).to_contain_text(item_txt)
    page.wait_for_timeout(2000)


