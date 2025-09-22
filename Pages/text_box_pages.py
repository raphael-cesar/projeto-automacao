from selenium.webdriver.common.by import By

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        # Locators
        self.FULL_NAME_INPUT = (By.ID, "userName")
        self.EMAIL_INPUT = (By.ID, "userEmail")
        self.CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
        self.PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
        self.SUBMIT_BUTTON = (By.ID, "submit")
        self.OUTPUT_DIV = (By.ID, "output")

    def navigate(self):
        self.driver.get(self.url)

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(full_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.CURRENT_ADDRESS_INPUT).send_keys(current_address)
        self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT).send_keys(permanent_address)

    def submit(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        # Rola até o botão e clica (boa prática que já aprendemos)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()

    def get_output_text(self):
        return self.driver.find_element(*self.OUTPUT_DIV).text