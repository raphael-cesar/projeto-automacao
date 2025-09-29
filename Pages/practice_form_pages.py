from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
        self.wait = WebDriverWait(self.driver, 10)
        #locators input
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.gender_radio = (By.XPATH, "//label[text()='{}']")
        self.mobile_input = (By.ID, "userNumber")
        self.dob_input = (By.ID, "dateOfBirthInput")
        self.subjects_input = (By.ID, "subjectsInput")
        self.hobbies_checkbox = (By.XPATH, "//label[text()='{}']")
        self.address_textarea = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")
        self.submit_button = (By.ID, "submit")
        self.out_put_modal = (By.ID, "example-modal-sizes-title-lg")
    
    def navigate(self):
        self.driver.get(self.url)

    def fill_form(self, data):
        # Subjects
        subjects_field = self.driver.find_element(*self.subjects_input)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", subjects_field)
        for subject in data["subjects"]:
            subjects_field.send_keys(subject)
            subjects_field.send_keys(Keys.ENTER)
            
        name_input = self.driver.find_element(*self.first_name_input)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", name_input)
        self.driver.find_element(*self.first_name_input).send_keys(data["first_name"])
        self.driver.find_element(*self.last_name_input).send_keys(data["last_name"])
        self.driver.find_element(*self.email_input).send_keys(data["email"])
        self.driver.find_element(By.XPATH, f"//label[text()='{data['gender']}']").click()
        self.driver.find_element(*self.mobile_input).send_keys(data["mobile"])
        
        # Date of Birth
        dob_field = self.driver.find_element(*self.dob_input)
        dob_field.send_keys(Keys.CONTROL + "a")
        dob_field.send_keys(data["dob"])
        dob_field.send_keys(Keys.ENTER)
        
        # Hobbies
        for hobby in data["hobbies"]:
            self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']").click()
            
        # State
        state_dropdown = self.driver.find_element(*self.state_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
        self.driver.find_element(*self.state_dropdown).click()
        self.driver.find_element(By.XPATH, f"//*[text()='{data['state']}']").click()
        
        #Adrees text field
        self.driver.find_element(*self.address_textarea).send_keys(data["address"])
        
        #City
        city_name = self.driver.find_element(*self.city_dropdown)
        self.driver.find_element(*self.city_dropdown).click()
        self.driver.find_element(By.XPATH, f"//*[text()='{data['city']}']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", city_name)
        self.driver.find_element(By.XPATH, f"//*[text()='{data['city']}']").click()

    def submit_form(self):
        button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.find_element(*self.submit_button).click()
    
    def check_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.out_put_modal)).is_displayed()
        #return self.driver.find_element(*self.out_put_modal).is_displayed()