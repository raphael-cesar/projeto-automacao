from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

class DroppableElements:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/droppable"
        
        self.interactions_button = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[5]")
        self.droppable_menu_button = (By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[5]/div/ul/li[4]/span")
        
        self.drag_object = (By.ID, "draggable")
        self.drop_object = (By.ID, "droppable")
        self.DROP_COLOUR = Color.from_string("#4682b4")
        
    def navigate_url(self):
        self.driver.get(self.url)
        # self.driver.find_element(*self.interactions_button).click()
        
        # drop_menu_bt = self.driver.find_element(*self.droppable_menu_button)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", drop_menu_bt)
        # self.driver.find_element(*self.droppable_menu_button).click()
        
    def drag_drop(self):
        actions = ActionChains(self.driver)
        drag_object = self.driver.find_element(*self.drag_object)
        drop_object = self.driver.find_element(*self.drop_object)
        actions.drag_and_drop(drag_object, drop_object).perform()
        
        login_button_background_colour = Color.from_string(drop_object.value_of_css_property('background-color'))
        drop_object_text = drop_object.text
        
        assert drop_object_text == "Dropped!"
        assert login_button_background_colour == self.DROP_COLOUR
        
    
        
        
    
        