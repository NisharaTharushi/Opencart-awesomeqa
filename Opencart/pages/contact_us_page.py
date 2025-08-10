from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ContactUsPage:
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.name_input = (By.NAME, "name")
        self.email_input = (By.NAME, "email")
        self.subject_input = (By.NAME, "subject")
        self.message_textarea = (By.ID, "message")
        self.upload_file = (By.NAME, "upload_file")
        self.submit_button = (By.NAME, "submit")
        self.success_msg = (By.XPATH, "//div[@class='status alert alert-success']")
        self.error_msg = (By.XPATH, "//div[contains(@class,'status alert-danger')]")


    
    print("---- Contact us page ----")
    def set_name(self, name):
        print("-- Contact Us Form --")  
        self.wait.until(EC.visibility_of_element_located(self.name_input)).clear()
        self.driver.find_element(*self.name_input).send_keys(name)
        print("name input value:",self.driver.find_element(*self.name_input).get_attribute("value"))

    def set_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email_input)).clear()
        self.driver.find_element(*self.email_input).send_keys(email)
        print("email input value:",self.driver.find_element(*self.email_input).get_attribute("value"))

    def set_subject(self, subject):
        self.wait.until(EC.visibility_of_element_located(self.subject_input)).clear()
        self.driver.find_element(*self.subject_input).send_keys(subject)
        print("subject input value:",self.driver.find_element(*self.subject_input).get_attribute("value"))

    def set_message(self, message):
        self.wait.until(EC.visibility_of_element_located(self.message_textarea)).clear()
        self.driver.find_element(*self.message_textarea).send_keys(message)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("message input value:",self.driver.find_element(*self.message_textarea).get_attribute("value"))
        time.sleep(2)

    def upload_file_path(self, file_path):
        # file_path should be absolute path to a file on your machine
        self.driver.find_element(*self.upload_file).send_keys(file_path)
        print("file input value:",self.driver.find_element(*self.upload_file).get_attribute("value"))
        time.sleep(2)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
        print("submit button clicked and page opened")
        time.sleep(2)

        # accept the alert 
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        print("page title:",self.driver.title)
        print("page url:",self.driver.current_url)

        print("")

        if "Success! Your details have been submitted successfully." in self.driver.page_source:
            print("Success! Your details have been submitted successfully. message displayed on the page.")
        else:
            print("Failure! Your details have not been submitted successfully.")    