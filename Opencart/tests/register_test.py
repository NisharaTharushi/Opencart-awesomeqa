import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from pages.register_page import Login

driver = webdriver.Firefox()
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")

register = Login(driver)

register.click_register_button()
register.fill_register_form(
    first_name="Test",
    last_name="User",
    email="LbE029g@example.com",  # Change email after each run
    telephone="1234567890",
    password="password",
    password_confirm="password",
)
register.change_account_info()
register.logout()

driver.quit()
