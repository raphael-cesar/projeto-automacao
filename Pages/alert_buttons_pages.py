from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsButton:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        self.wait = WebDriverWait(self.driver, 10)
        
        self.forms_button = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]")
        self.alert_menu_button = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/span/div/div[1]")
        self.alert_button = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[2]")
        
        self.see_alert_button = (By.ID, "alertButton")
        self.five_seconds_alert_button = (By.ID, "timerAlertButton") 
        
        self.options_alert_button = (By.ID, "confirmButton")
        self.options_alert_text = (By.ID, "confirmResult")
        
        self.input_name_alert_button= (By.ID, "promtButton")
        self.output_name_alert_text = (By.ID, "promptResult")
        
        
    def navigate(self):
        self.driver.get(self.url)
        self.driver.find_element(*self.forms_button).click()
        self.driver.find_element(*self.alert_menu_button).click()
        self.wait.until(EC.element_to_be_clickable(self.alert_button)).click()
        
    def see_alert(self, expected_text):
        self.driver.find_element(*self.see_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == expected_text
        alert.accept()
        
    def five_seconds_alert(self, expected_text):
        self.driver.find_element(*self.five_seconds_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == expected_text
        alert.accept() 
        
    def options_alert_accept(self, expected_text):
        self.driver.find_element(*self.options_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.accept() 
        alert_text = self.driver.find_element(*self.options_alert_text).text
        assert alert_text == expected_text 
    
    def options_alert_dismiss(self, expected_text):
        self.driver.find_element(*self.options_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss() 
        alert_text = self.driver.find_element(*self.options_alert_text).text
        assert alert_text == expected_text 
        
    def input_name_alert(self, expected_text, expected_name):
        self.driver.find_element(*self.input_name_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(expected_name)
        alert.accept() 
        alert_text = self.driver.find_element(*self.output_name_alert_text).text
        assert alert_text == expected_text 