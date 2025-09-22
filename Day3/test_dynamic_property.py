import time
from selenium.webdriver.common.by import By

def test_dinamic_button(driver):

    driver.get("https://demoqa.com/elements")

    dynamic_property = driver.find_element(By.ID, "item-8")
    
    driver.execute_script("arguments[0].scrollIntoView(true);", dynamic_property)

    assert dynamic_property.is_displayed()
    dynamic_property.click()
    
    time.sleep(6)

    visible_After_button = driver.find_element(By.ID, "visibleAfter")
    visible_After_button.click()
