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
    TITLE = "Your Store"
    LOGO = (By.XPATH, "//img[@title='TheTestingAcademy eCommerce']")
    HEADER = (By.XPATH, "//nav[@id='top']//div[@class='container']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
    EURO = (By.XPATH, "//button[contains(text(),'€ Euro')]")
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle strong")
    CONTACT_INFO = (By.XPATH, "//i[@class='fa fa-phone']")
    ACCOUNT_INFO = By.LINK_TEXT, "My Account"
    REGISTER_BUTTON = By.LINK_TEXT, "Register"
    LOGIN_BUTTON = By.LINK_TEXT, "Login"
    WISHLIST_BUTTON = By.ID , "wishlist-total"
    CART_BUTTON = By.LINK_TEXT, "Shopping Cart"
    CHECKOUT_BUTTON = By.LINK_TEXT, "Checkout"

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
    # <section id="//body//footer" class=
    FOOTER = (By.XPATH, "//body//footer")
    def get_title(self):
        return self.driver.title
    
    def get_logo(self):
        logo = self.driver.find_element(*self.LOGO)
        print("Logo:",logo.get_attribute("src"))

    def get_displayed_currency_symbol(self):
        currency_symbol = self.driver.find_element(*self.CURRENCY_SYMBOL)
        print(currency_symbol.text)
        print("Displayed currency symbol")
        print("")

    def select_currency(self):
        currency_dropdown = self.driver.find_element(*self.CURRENCY_DROPDOWN)
        currency_dropdown.click()
        self.driver.find_element(*self.EURO).click()
        print("Currency changed to Euro")
        print("")

    def curreny_icon(self):
        currency_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-toggle='dropdown']")

        # 2. Verify button is displayed
        assert currency_button.is_displayed(), "Currency button is not visible."
        print("✅ Currency button is visible.")

        # 3. Verify £ symbol is displayed
        currency_symbol = currency_button.find_element(By.TAG_NAME, "strong").text.strip()
        assert currency_symbol == "£", f"❌ Expected currency symbol '£', but found '{currency_symbol}'"
        print("✅ Default currency symbol is correct:", currency_symbol)

        # 4. Verify label 'Currency' is present (if not hidden by screen size)
        try:
            label = currency_button.find_element(By.CLASS_NAME, "hidden-xs").text.strip()
            assert label == "Currency", f"❌ Expected label 'Currency', got '{label}'"
            print("✅ Currency label is correct:", label)
        except Exception:
            print("⚠️ Currency label might be hidden on small screen.")

        # 5. Verify dropdown icon is visible
        dropdown_icon = currency_button.find_element(By.CSS_SELECTOR, "i.fa.fa-caret-down")
        assert dropdown_icon.is_displayed(), "❌ Dropdown icon is not visible."
        print("✅ Dropdown icon is visible.")

        # 6. Click the button to open the dropdown
        currency_button.click()
        time.sleep(1)

        # 7. Verify dropdown menu appears with currency options
        currency_options = self.driver.find_elements(By.CSS_SELECTOR, "ul.dropdown-menu li button")
        assert len(currency_options) > 0, "❌ No currency options found in dropdown."
        print("✅ Dropdown opened. Found currency options:")
        for option in currency_options:
            print(" -", option.text.strip())
               
    def get_header(self):
        print("---- Header Links ----")
        header = self.driver.find_element(*self.HEADER)
        for link in header.find_elements(By.TAG_NAME, "a"):
            print("text:",link.text)
            print("innerText:",link.get_attribute("innerText"))
            print("href: ",link.get_attribute("href"))
            print("")

    def click_contact_info(self):
        print("---- Contact Info button ----")
        contact_info = self.driver.find_element(*self.CONTACT_INFO)
        contact_info.click()
        print("Contact info clicked and page opened",self.driver.current_url)
        print("")

    def click_account_info(self):
        print("---- Account Info button ----")
        account_info = self.driver.find_element(*self.ACCOUNT_INFO)
        account_info.click()
        print("Account info clicked and page opened",self.driver.current_url)
        print("")

    def click_register_button(self):
        print("---- Register Button ----")
        self.driver.find_element(*self.ACCOUNT_INFO).click()
        self.driver.find_element(*self.REGISTER_BUTTON).click() #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.LINK_TEXT, "Register")))
        print("Register button clicked and page opened",self.driver.current_url)        
    
    def click_login_button(self):
        print("---- Login Button ----")
        self.driver.find_element(*self.ACCOUNT_INFO).click()
        self.driver.find_element(*self.LOGIN_BUTTON).click() #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.LINK_TEXT, "Login")))
        print("Login button clicked and page opened",self.driver.current_url)

    def click_wishlist_button(self):
        print("---- Wishlist Button ----")
        wishlist_button = self.driver.find_element(*self.WISHLIST_BUTTON)
        wishlist_button.click()
        print("Wishlist button clicked and page opened",self.driver.current_url)
        self.driver.back()
        print("")

    def click_cart_button(self):
        print("---- Cart Button ----")
        cart_button = self.driver.find_element(*self.CART_BUTTON)
        cart_button.click()
        print("Cart button clicked and page opened",self.driver.current_url)
        self.driver.back()
        print("")

    def click_checkout_button(self):
        print("---- Checkout Button ----")
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_button.click()
        print("Checkout button clicked and page opened",self.driver.current_url)
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
        print("---- Click All Categories ----")
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

    def search_for_product(self, product_name):
        print("---- Search for Product ----")
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(product_name)
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
        search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
        for result in search_results:
            print(result.text)
        print("Search results displayed and page opened",self.driver.current_url)   
        self.driver.back()
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
            
