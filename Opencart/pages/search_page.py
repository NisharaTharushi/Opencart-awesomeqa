from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Home():
    def __init__(self, driver):
        self.driver = driver
        

    # Locators
    SEARCH_INPUT = By.NAME, "search"
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".product-thumb")
    
    DESKTOPS_CATEGORY = (By.XPATH, "//a[normalize-space()='Desktops']")
    LAPTOPS_CATEGORY = (By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
    COMPONENTS_CATEGORY = (By.XPATH, "//a[normalize-space()='Components']")
    TABLETS_CATEGORY = (By.XPATH, "//a[normalize-space()='Tablets']")
    SOFTWARE_CATEGORY = (By.XPATH, "//a[normalize-space()='Software']")
    PHONES_CATEGORY = (By.XPATH, "//a[normalize-space()='Phones & PDAs']")
    CAMERAS_CATEGORY = (By.XPATH, "//a[normalize-space()='Cameras']")
    MP3_PLAYERS_CATEGORY = (By.XPATH, "//a[normalize-space()='MP3 Players']")

    FOOTER = (By.XPATH, "//body//footer")
    

    def search_for_product(self, product_name):
        print("---- Search for Product ----")
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(product_name)
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
        search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
        for result in search_results:
            print(result.text)
        print("Search results displayed and page opened",self.driver.current_url)   
        self.driver.back()
        print("")

    def get_menu(self):
        print("---- Menu List ----")
        menu = self.driver.find_element(*self.MENU)
        print("text:",menu.text)
        print("innerText:",menu.get_attribute("innerText"))
        print("href: ",menu.get_attribute("href"))
        print("")

    def click_all_categories(self):
        base_url = "https://awesomeqa.com/ui/index.php?route=common/home"

        categories = self.driver.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown > a.dropdown-toggle")
        num_categories = len(categories) # Get the number of categories

        for i in range(num_categories):
            self.driver.get(base_url)
            time.sleep(2)

            # Re-find categories fresh on every iteration
            categories = self.driver.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown > a.dropdown-toggle")
            category = categories[i] # Get the current category

            # Skip MP3 Players category if needed
            if category.text.strip() == "MP3 Players":
                print("MP3 Players category found — stopping the loop.")
                break

            category.click()
            time.sleep(1)

            # Re-find dropdown parent and sub-links fresh
            parent_li = category.find_element(By.XPATH, "..") # Re-find dropdown parent
            sub_links = parent_li.find_elements(By.CSS_SELECTOR, "div.dropdown-menu ul.list-unstyled li a")
            num_sub_links = len(sub_links) # Get the number of sub-links

            for j in range(num_sub_links):
                # Reload the page and re-open dropdown before each sub-link click
                self.driver.get(base_url)
                time.sleep(2)

                categories = self.driver.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li.dropdown > a.dropdown-toggle")
                category = categories[i] # Get the current category
                category.click()
                time.sleep(1)

                parent_li = category.find_element(By.XPATH, "..") # Re-find dropdown parent
                # Re-find sub-links fresh
                sub_links = parent_li.find_elements(By.CSS_SELECTOR, "div.dropdown-menu ul.list-unstyled li a")
                sub_link = sub_links[j] # Get the current sub-link

                href = sub_link.get_attribute("href")
                print(f"Clicking link: {href}")

                sub_link.click()
                time.sleep(2)

                print("Link clicked and page opened",self.driver.current_url)
                
                subcategory_name_on_page = self.driver.find_element(By.TAG_NAME, "h2").text.strip()
                print(f"Subcategory page title: '{subcategory_name_on_page}'")

                self.driver.back()
                time.sleep(2)

    
    def click_tabs_category(self):
        print("---- Tabs Category ----")
        tabs_category = self.driver.find_element(*self.TABLETS_CATEGORY)
        tabs_category.click()
        print("Tabs category clicked and page opened",self.driver.current_url)
        print("")

    def click_software_category(self):
        print("---- Software Category ----")
        software_category = self.driver.find_element(*self.SOFTWARE_CATEGORY)
        software_category.click()
        print("Software category clicked and page opened",self.driver.current_url)
        print("")

    def click_phones_category(self):
        print("---- Phones Category ----")
        phones_category = self.driver.find_element(*self.PHONES_CATEGORY)
        phones_category.click()
        print("Phones category clicked and page opened",self.driver.current_url)
        print("")

    def click_cameras_category(self):
        print("---- Cameras Category ----")
        cameras_category = self.driver.find_element(*self.CAMERAS_CATEGORY)
        cameras_category.click()
        print("Cameras category clicked and page opened",self.driver.current_url)
        print("")

    def click_MP3_players_category(self):
        print("---- MP3 Players Category ----")
        mp3_players_category = self.driver.find_element(*self.MP3_PLAYERS_CATEGORY)
        mp3_players_category.click()
        print("MP3 Players category clicked and page opened",self.driver.current_url)
        print("")


    def footer(self):
        print("---- Footer ----")
        base_url = "https://awesomeqa.com/ui/index.php?route=common/home"
        self.driver.get(base_url)
        time.sleep(2)

        # Locate all footer links inside the footer container
        footer_links = self.driver.find_elements(By.CSS_SELECTOR, "footer a")

        print(f"Found {len(footer_links)} footer links.")

        for i in range(len(footer_links)):
            self.driver.get(base_url)
            time.sleep(2)
            
            # Re-find footer links because page reloads break old references
            footer_links = self.driver.find_elements(By.CSS_SELECTOR, "footer a")
            link = footer_links[i]
            
            link_text = link.text.strip()
            href = link.get_attribute("href")
            
            print(f"\nClicking footer link: '{link_text}' | URL: {href}")
            
            link.click()
            time.sleep(2)
            
            print("Page URL after click:", self.driver.current_url)
            
