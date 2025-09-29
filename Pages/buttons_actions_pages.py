from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ButtonsActions():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/buttons"
        self.action = ActionChains(self.driver)
        
        #locators
        self.double_click_btn = (By.ID, "doubleClickBtn")
        self.right_click_btn = (By.ID, "rightClickBtn")
        self.dynamic_click_btn = (By.XPATH, "//button[text()='Click Me']")
        
        #validators
        self.double_click_message = (By.ID, "doubleClickMessage")
        self.right_click_message = (By.ID, "rightClickMessage")
        self.dynamic_click_message = (By.ID, "dynamicClickMessage")
        
    def navigate(self):
        self.driver.get(*self.url)
        
    def double_click(self):
        double_click_button = self.driver.find_element(*self.double_click_btn)
        self.action.double_click(double_click_button).perform()
        
    # def check_double_click(self):
        