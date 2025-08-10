import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import Login

driver = webdriver.Firefox() 
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")

register = Login(driver)

register.click_login_page()
register.fill_login_form(
    email="LbE05577335g@example.com",
    password="password"
)

driver.quit()

