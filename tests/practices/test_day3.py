'''
XPath -> XML Path
'''


from playwright.sync_api import Page, expect


def test_day3(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # #1. Absole Path (Full XPath)
    # logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    # expect(logo).to_be_utvisible()
    # page.wait_for_timeout(5000)

    #2. Relative Path //tagname[@attribute='value']
    # logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    # expect(logo).to_be_visible()
    # page.wait_for_timeout(5000)


    products = page.locator("//h2//a[contains(@href,'computer')]")
    products_count=products.count()
    # print(f"products_count: {products_count}")
    expect(products).to_have_count(products_count)

    # print(f"First computer product: ",products.first.text_content())
    # print(f"Last computer product: ",products.last.text_content())
    # print(f"nth computer product: ", products.nth(2).text_content())

    products_titles = products.all_text_contents()
    print(f"Products titles: ",products_titles)

    print("Printing product titles using loop statement")
    for p in products_titles:
        print(p)


    #XPath start-with()
    building_product = page.locator("//h2//a[starts-with(@href,'/build')]")
    print(f"Building product: ",building_product.count())
    expect(building_product).to_have_count(building_product.count())


    #XPath with text() -- it represent inner text of element
    register_link = page.locator("//a[text()='Register']")
    expect(register_link).to_be_visible()


    #XPath with last()
    googleplus_link = page.locator("//div[@class='column follow-us']//li[last()]")  #//div[@class='column follow-us']//li[5]
    expect(googleplus_link).to_have_text("Google+")


    #Xpath with position()
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")  #//div[@class='column follow-us']//li[5]
    expect(twitter_link).to_have_text("Twitter")


def test_handling_dynamic_elements(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    # page.wait_for_timeout(3000)

    for i in range(5):
        button=page.locator("//button[text()='START' or text()='STOP']")
        button.click()
        page.wait_for_timeout(2000)

