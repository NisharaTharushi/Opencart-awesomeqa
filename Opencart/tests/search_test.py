import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.search_page import Home

driver = webdriver.Firefox() 
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
home = Home(driver)

# Search for a product, e.g., Macbook
home.search_for_product("Macbook")

driver.get("https://awesomeqa.com/ui/index.php?route=common/home")

# Search for another product, e.g., iPhone
home.search_for_product("iPhone")

driver.quit()




