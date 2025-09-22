import os #used to use commands related to the operating system
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_button_clicks_with_screenshots(driver):
    if not os.path.exists("Screenshots"):
        os.makedirs("Screenshots")

    driver.get("https://demoqa.com/buttons")
    
    actions = ActionChains(driver)

    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    
    actions.double_click(double_click_btn).perform()
    driver.save_screenshot("screenshots/1_after_double_click.png")
    double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    assert "You have done a double click" in double_click_message.text
