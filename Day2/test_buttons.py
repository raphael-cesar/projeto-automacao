from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_double_click_button(driver):
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    # 1. Double Click
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    assert "You have done a double click" in double_click_message.text

def test_right_click_button(driver):
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    # 2. Right Click
    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    right_click_message = driver.find_element(By.ID, "rightClickMessage")
    assert "You have done a right click" in right_click_message.text

def test_dynamic_click_button(driver):
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    
     # 3. Dynamic Click (Simple)
    # This button has a dynamic ID, so we use a more robust locator
    dynamic_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    dynamic_click_btn.click()
    dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage")
    assert "You have done a dynamic click" in dynamic_click_message.text
    time.sleep(3)
