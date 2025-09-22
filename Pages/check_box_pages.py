from selenium.webdriver.common.by import By

class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"
        #locators
        self.expand_all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.commands_checkbox = (By.XPATH, "//label[@for='tree-node-commands']")
        self.commands_checkbox_output = (By.ID, "tree-node-commands")
        
    def navigate(self):
        self.driver.get(self.url)
        
    def expand_all(self):
        self.driver.find_element(*self.expand_all_button).click()
    
    def select_check_box(self):
        self.driver.find_element(*self.commands_checkbox).click()

    def get_selected_element(self):
        check_box_element = self.driver.find_element(*self.commands_checkbox_output)
        return check_box_element.is_selected()