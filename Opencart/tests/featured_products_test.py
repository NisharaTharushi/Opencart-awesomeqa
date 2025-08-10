import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.featured_products import Home


driver = webdriver.Firefox() 
driver.get("https://awesomeqa.com/ui/index.php?route=common/home")


home = Home(driver)

home.get_title()
home.test_all_products()

driver.quit()



