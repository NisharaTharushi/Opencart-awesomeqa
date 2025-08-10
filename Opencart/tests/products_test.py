
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.home_page import Home

driver = webdriver.Firefox() 
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")

home = Home(driver)

home.click_all_categories()
home.click_tabs_category()
home.click_software_category()
home.click_phones_category()
home.click_cameras_category()
home.click_MP3_players_category()

driver.quit()




