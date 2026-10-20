from playwright.sync_api import Page  , expect
from config import * 
import time

class Login:
    
    def __init__(self , page:Page):
        self.page = page
        
        
    def validLogin(self):
        self.page.goto(BaseUrl) 
        time.sleep(2) 
        
        self.page.get_by_label('Username').type('student' , delay=180)
        time.sleep(2) 
        
        self.page.get_by_label('Password').type('Password123' , delay=180)
        time.sleep(2) 
        
        self.page.get_by_role('button' , name='Submit').click()
        time.sleep(2)
        