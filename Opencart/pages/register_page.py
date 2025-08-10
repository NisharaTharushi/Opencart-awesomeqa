from selenium.webdriver.common.by import By


class Login:
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
    # <input type="submit" value="Continue" class="btn btn-primary">
    Continue_button = By.XPATH, "//input[@value='Continue']"
    Edit_your_account_information = By.LINK_TEXT, "Edit your account information"
    login_page = By.LINK_TEXT, "Login"
    Logout = By.LINK_TEXT, "Logout"

    print("---- Register page ----")

    # click account dropdown and open Register form
    def click_register_button(self):
        print("-- Register buttons --")
        self.driver.find_element(*self.Dropdown).click()
        # select Register from account dropdown
        self.driver.find_element(*self.Register).click()
        print(
            "Register button clicked in Account dropdown and Register page opened",
            self.driver.current_url,
        )

        # # click continue button
        # self.driver.find_element(*self.Continue).click()
        # print(" Continue button clicked and Register page opened",self.driver.current_url)

        # # click register button
        # self.driver.find_element(*self.Register_button).click()
        # print("Register button clicked in the side menu and Register page opened again",self.driver.current_url)
        # time.sleep(2)
        # print("")

    def fill_register_form(
        self, first_name, last_name, email, telephone, password, password_confirm
    ):
        # First Name
        self.driver.find_element(*self.First_name).send_keys(first_name)
        # Last Name
        self.driver.find_element(*self.Last_name).send_keys(last_name)
        # Email
        self.driver.find_element(*self.Email).send_keys(email)
        # Telephone
        self.driver.find_element(*self.Telephone).send_keys(telephone)
        # Password
        self.driver.find_element(*self.Password).send_keys(password)
        # Password confirm
        self.driver.find_element(*self.Password_confirm).send_keys(password_confirm)
        # Subscribe
        self.driver.find_element(*self.Subscribe).click()
        # Privacy
        self.driver.find_element(*self.Privacy).click()
        # Continue
        self.driver.find_element(*self.Continue_button).click()
        print("Register page completed")

        # test if the Your Account Has Been Created! message is displayed
        # assert "Your Account Has Been Created!" in self.driver.page_source
        if "Your Account Has Been Created" in self.driver.page_source:
            print("Your Account Has Been Created! message is displayed")
        else:
            print("Your Account Has Been Created! message is not displayed")

        # click continue button
        self.driver.find_element(*self.Continue).click()

        # test if My Account is displayed
        if "My Account" in self.driver.page_source:
            print("My Account is displayed")
        else:
            print("My Account is not displayed")
        print("")

    def change_account_info(self):
        # click Edit your account information
        print("-- Edit your account information --")
        self.driver.find_element(*self.Edit_your_account_information).click()

        # First Name change after clear
        self.driver.find_element(*self.First_name).clear()
        self.driver.find_element(*self.First_name).send_keys("Nishara")
        print("First Name changed")

        # Last Name change after clear
        self.driver.find_element(*self.Last_name).clear()
        self.driver.find_element(*self.Last_name).send_keys("Tharushi")
        print("Last Name changed")

        # Email change after clear
        self.driver.find_element(*self.Email).clear()
        self.driver.find_element(*self.Email).send_keys("NfP9n@example.com")
        print("Email changed")

        # Continue
        self.driver.find_element(*self.Continue_button).click()
        print("Account info changed")
        print("")

    def logout(self):
        print("-- Logout --")
        # click logout button from Account dropdown
        self.driver.find_element(*self.Dropdown).click()
        # select Logout from account dropdown
        self.driver.find_element(*self.Logout).click()
        print("Logout button clicked and page opened", self.driver.current_url)
        print("")

        # test if Account Logout! message is displayed
        if "Account Logout" in self.driver.page_source:
            print("Account Logout! message is displayed")
        else:
            print("Account Logout! message is not displayed")

        # click continue button
        self.driver.find_element(*self.Continue).click()

    def click_login_page(self, email, password):
        # select Login from account dropdown
        self.driver.find_element(*self.login_page).click()
        print("Login page opened", self.driver.current_url)
        print("")

        # fill email and password
        self.driver.find_element(*self.Email).send_keys(email)
        self.driver.find_element(*self.Password).send_keys(password)

        # click login button
        self.driver.find_element(*self.Continue).click()
        print("Login button clicked and page opened", self.driver.current_url)
        print("")
