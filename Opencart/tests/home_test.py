import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.home_page import Home

driver = webdriver.Firefox() 
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")

home = Home(driver)

home.get_title()
home.get_logo()
home.get_displayed_currency_symbol()
home.select_currency()
home.get_header()
home.click_contact_info()
home.click_register_button()
home.click_login_button()
home.click_wishlist_button()
home.click_cart_button()
home.click_checkout_button()
home.search_for_product("Macbook")

home.click_all_categories()
home.click_tabs_category()
home.click_software_category()
home.click_phones_category()
home.click_cameras_category()
home.click_MP3_players_category()

home.footer()

driver.quit()




