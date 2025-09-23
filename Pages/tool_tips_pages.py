from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ToolTipsPage:
    def __init__(self, driver):
        self.driver = driver
        #self.url = "https://demoqa.com/tool-tips"
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        
        # Locators
        self.tool_tips_button = (By.ID, "toolTipButton")
        self.tool_tips_text_field = (By.ID, "toolTipTextField")
        self.tool_tips_text_message = (By.CLASS_NAME, "tooltip-inner")
        
    def navigate(self, url):
        self.driver.get(url)
        
    def hover_over_button(self):
        button = self.driver.find_element(*self.tool_tips_button)
        self.action.move_to_element(button).perform()
           
    def is_hover_tool_tips_button_correct(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self.tool_tips_text_message)).text
        return actual_text == expected_text

    def hover_over_text_field(self):
        text_field = self.driver.find_element(*self.tool_tips_text_field)
        self.action.move_to_element(text_field).perform()
    
    def is_hover_tool_tips_text_field_correct(self, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(self.tool_tips_text_message)).text
        return actual_text == expected_text
