from playwright.sync_api import sync_playwright  , Page
import time , pytest  
from config import * 

class InvalidLogin:
    
    def __init__(self , page:Page):
        self.page = page 
        
    def invalid_login(self):
        self.page.goto(BaseUrl) 
        time.sleep(2) 
        
        self.page.get_by_label('Username').type('Student' , delay=100)
        time.sleep(2) 
        
        self.page.get_by_label('Password').type('Password123' , delay=100)
        time.sleep(2) 
        
        self.page.get_by_role('button' , name='Submit').click()
        time.sleep(2)
                