from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ModalDialoguePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        #locators
        self.small_modal_button = (By.ID, "showSmallModal")
        self.large_modal_button = (By.ID, "showLargeModal")
        self.modal_large_text_info = (By.ID, "example-modal-sizes-title-lg")
        self.modal_small_text_info = (By.ID, "example-modal-sizes-title-sm")
        
    def navigate(self, url):
        self.driver.get(url)
        
    def click_small_modal_button(self):
        self.driver.find_element(*self.small_modal_button).click()
        
    def is_small_modal_displayed(self):
        # wait for the small modal title element to be visible and return whether it's displayed
        return self.wait.until(EC.visibility_of_element_located(self.modal_small_text_info)).is_displayed()
    
    def click_large_modal_button(self):
        self.driver.find_element(*self.large_modal_button).click()
        
    def is_large_modal_displayed(self, expected_text: str) -> bool:
        # wait for the large modal title element, get its text and compare to expected_text
        el = self.wait.until(EC.visibility_of_element_located(self.modal_large_text_info))
        actual_text = el.text.strip()
        return actual_text == expected_text
    
    