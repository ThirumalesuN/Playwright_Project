from playwright.sync_api import sync_playwright 
import pytest 


@pytest.fixture
def openBrowser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome' , headless=False)
        context = browser.new_context() 
        page = context.new_page() 
        yield page 
        browser.close()