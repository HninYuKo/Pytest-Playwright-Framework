from playwright.sync_api import Page, expect


def test_frame_sample(page: Page) -> None:
    page.goto("https://ui.vision/demo/webtest/frames/")
    page.wait_for_timeout(3000)


    frames = page.frames
    print("Number of frames on a page :: ",len(frames)) #7

    #frame 1
    frame1=page.frame_locator("frame[src='frame_1.html']") #get the frame approach 1

    # frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html") # get the frame approach 2
    # frame1=page.frame("name of the frame")# get the frame approach 3
    frame1.locator("input[name='mytext1']").fill("Welcome to Myanmar")
    page.wait_for_timeout(3000)