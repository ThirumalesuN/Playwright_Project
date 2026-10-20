from Pages.login_page import Login

def test_valid_login(openBrowser):
    driver = Login(openBrowser) 
    driver.validLogin() 
    print("Congrats...")