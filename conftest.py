import os
import sys
import pytest
from playwright.sync_api import sync_playwright
# in conftest.py (modify your existing page_instance fixture)
from pathlib import Path
from uuid import uuid4
import re

# # 1. Fix "ModuleNotFoundError: No module named 'pages'"
# root_dir = os.path.dirname(os.path.abspath(__file__))
# if root_dir not in sys.path:
#     sys.path.insert(0, root_dir)


# 2. Register the custom CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",  # The command-line flag name
        action="store",
        default="chromium",  # Default browser if the flag is omitted
        choices=["chromium", "firefox"],  # Restrict inputs to valid engines
        help="Browser type to execute tests on: chromium, firefox"
    )


# 3. Create a helper fixture to retrieve the CLI value
@pytest.fixture(scope="session")
def browser_type_name(request):
    # Retrieve the command line value parsed by pytest
    return request.config.getoption("--browser-name")


# 4. Dynamically launch the requested browser instance based on the CLI option
@pytest.fixture(scope="session")
def browser_instance(browser_type_name):
    with sync_playwright() as p:
        print(f"\n[Setup] CLI requested: {browser_type_name.upper()}. Launching instance...")

        # Dynamically switch browser engine
        if browser_type_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_type_name == "firefox":
            browser = p.firefox.launch(headless=False)
        # elif browser_type_name == "webkit":
        #     browser = p.webkit.launch(headless=False) # Playwright does not support webkit on mac13
        else:
            raise ValueError(f"Unsupported browser: {browser_type_name}")

        yield browser

        print(f"\n[Teardown] Closing {browser_type_name.upper()} browser instance...")
        browser.close()


# # 5. Downstream standard page fixture for test functions
# @pytest.fixture(scope="function")
# def page_instance(browser_instance):
#     context = browser_instance.new_context()
#     page = context.new_page()
#     yield page
#     context.close()




def _safe_name(nodeid: str) -> str:
    # simple sanitize for filesystem names
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", nodeid)

@pytest.fixture(scope="function")
def page_instance(browser_instance, request):
    trace_dir = Path("test-results")
    trace_dir.mkdir(parents=True, exist_ok=True)

    context = browser_instance.new_context()
    # create a unique trace file per test
    trace_file = trace_dir / f"trace-{uuid4().hex}.zip"
    # trace_file = trace_dir / f"{_safe_name(request.node.nodeid)}-{uuid4().hex}.zip"

    # start tracing (screenshots, snapshots, sources are typical useful options)
    context.tracing.start(title=request.node.nodeid, screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    # stop tracing and save into test-results
    context.tracing.stop(path=str(trace_file))

    # close context
    context.close()

# @pytest.fixture(scope="session")
# def browser():
#    with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False) #with headed
#        # browser = p.chromium.launch(headless=True) #no headed
#        yield browser
#        browser.close()
#
# @pytest.fixture
# def page(browser):
#    page = browser.new_page()
#    yield page
#    page.close()