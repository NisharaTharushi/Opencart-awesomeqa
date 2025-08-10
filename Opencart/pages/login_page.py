from selenium.webdriver.common.by import By



class Login():
    def __init__(self, driver):
        self.driver = driver

    Dropdown = By.LINK_TEXT, "My Account"
    Register = By.LINK_TEXT, "Register"
    Continue = By.LINK_TEXT, "Continue"
    First_name = By.ID, "input-firstname"
    Last_name = By.ID, "input-lastname"
    Email = By.ID, "input-email"
    Telephone = By.ID, "input-telephone"
    Password = By.ID, "input-password"
    Password_confirm = By.ID, "input-confirm"
    # <input type="radio" name="newsletter" value="1">
    Subscribe = By.XPATH, "//input[@name='newsletter' and @value='1']"
    # <input type="checkbox" name="agree" value="1">
    Privacy = By.XPATH, "//input[@name='agree' and @value='1']"
    #<input type="submit" value="Continue" class="btn btn-primary">
    Continue_button = By.XPATH, "//input[@value='Continue']"
    Edit_your_account_information = By.LINK_TEXT, "Edit your account information"
    login_page = By.LINK_TEXT, "Login"
    Logout = By.LINK_TEXT, "Logout"


    print("---- Login page ----")
    # click account dropdown and open Register form
    def click_login_page(self):    
        # select Login from account dropdown'
        self.driver.find_element(*self.Dropdown).click()
        self.driver.find_element(*self.login_page).click()    
        print("Login page opened",self.driver.current_url)
        print("")
    
    def fill_login_form(self, email, password):
        # fill email and password
        self.driver.find_element(*self.Email).send_keys(email )
        self.driver.find_element(*self.Password).send_keys(password)

        # click login button
        self.driver.find_element(*self.Continue).click()
        print("Login button clicked and page opened",self.driver.current_url)
        print("")

    def logout(self):    
        # click logout button from Account dropdown
        self.driver.find_element(*self.Dropdown).click()
        # select Logout from account dropdown
        self.driver.find_element(*self.Logout).click()
        print("Logout button clicked and page opened",self.driver.current_url)
        print("")

        # test if Account Logout! message is displayed
        if "Account Logout" in self.driver.page_source:
            print("Account Logout! message is displayed")
        else:
            print("Account Logout! message is not displayed")

        # click continue button
        self.driver.find_element(*self.Continue).click()