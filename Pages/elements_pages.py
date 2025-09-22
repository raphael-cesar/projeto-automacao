from selenium.webdriver.common.by import By

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        # locators
        self.menu_box_id = (By.ID, "item-0")
        self.menu_box_css = (By.CSS_SELECTOR, "#item-0")
        self.menu_box_xpath = (By.XPATH, "//span[text()='Text Box']")
        
    def navigate(self):
        self.driver.get(self.url)
    
    def is_check_box_id_displayed(self):
        return self.driver.find_element(*self.menu_box_id).is_displayed()
    
    def is_check_box_css_displayed(self):
        return self.driver.find_element(*self.menu_box_css).is_displayed()
    
    def is_check_box_xpath_displayed(self):
        return self.driver.find_element(*self.menu_box_xpath).is_displayed()

    def is_check_box_text_correct(self, expected_text):
        actual_text = self.driver.find_element(*self.menu_box_id).text
        return actual_text == expected_text