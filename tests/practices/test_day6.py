
import re
from playwright.sync_api import Page, expect


def test_day6(page: Page) -> None:

    page.goto("https://testautomationpractice.blogspot.com")
    # page.wait_for_timeout(3000)
    # #3 ways to select option from drop down
    page.locator("#country").select_option("India") # by label
    # # page.locator("#country").select_option(label="India")  # by label
    # page.wait_for_timeout(2000)
    # page.locator("#country").select_option("germany")  # by value
    # # page.locator("#country").select_option(value="germany")  # by value
    #
    # page.wait_for_timeout(2000)
    # page.locator("#country").select_option(index=5) #by index # index start from 0
    #
    page.wait_for_timeout(3000)

    #check number of options in dropdown
    dropdown_options=page.locator("#country option")
    expect(dropdown_options).to_have_count(10)

    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    # print(f"options_text: {options_text}")

def test_multiselect_down(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com")
    page.wait_for_timeout(3000)
    #select multiple options from dropdown 3 way
    # page.locator("#colors").select_option(["Red", "Blue", "Green"]) # by label
    # page.locator("#colors").select_option(label=["Red","Blue","Yellow"]) # by label

    # page.locator("#colors").select_option(["red","blue","yellow"]) # by value
    # page.locator("#colors").select_option(value=["red","blue","yellow"]) # by value

    # page.locator("#colors").select_option(index=[0,1,4]) # by index
    page.wait_for_timeout(3000)


def test_multiselect_down_sorted(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com")
    page.wait_for_timeout(3000)
    # dropdown_options=page.locator("#animals option")
    dropdown_options=page.locator("#country option")
    expect(dropdown_options).to_have_count(10)
    options_text=[text.strip() for text in dropdown_options.all_text_contents()]

    original_options=options_text.copy()
    sorted_options=sorted(options_text) #    sorted_options=sorted(options_text,reverse=True) decending sorting

    print(f"original_options: {original_options}")
    print(f"sorted_options: {sorted_options}")

    if original_options == sorted_options:
        print("drop down are sorted correctly")
        # assert True
    else:
        print("drop down are not sorted correctly")
        # assert False

def test_bstackdemo_sort(page: Page) -> None:

    page.goto("https://bstackdemo.com/")
    page.wait_for_timeout(3000)

    page.locator("div[class='sort'] select").select_option("lowestprice") # low to high
    page.wait_for_timeout(3000)

    prices_list=page.locator(".shelf-item__price .val b").all_text_contents()
    # print(f"prices_list: {prices_list}")
    title_list=page.locator("p[class='shelf-item__title']").all_text_contents()
    # print(f"title_list: {title_list}")
    # print(f"length of title_list: {len(title_list)}")
    expect(prices_list).to_have_count(25)

    for i in range(len(title_list)):
        print(f"title: {title_list[i]} , price: {prices_list[i]}")

    lowest_title=title_list[0]
    lowest_price=prices_list[0]
    print(f"lowest_title: {lowest_title}, lowest_price: {lowest_price}")

    highest_title=title_list[-1]
    highest_price=prices_list[-1]
    print(f"highest_title: {highest_title}, highest_price: {highest_price}")
