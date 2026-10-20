from Pages.invalid_login import InvalidLogin

def test_invalid(openBrowser):
    driver = InvalidLogin(openBrowser)
    driver.invalid_login()