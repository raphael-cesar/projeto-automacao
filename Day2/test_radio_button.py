from selenium.webdriver.common.by import By

def test_interact_with_radio_button(driver):

    driver.get("https://demoqa.com/radio-button")
    
    # Radio buttons may be disabled or hidden, which requires a click via JavaScript
    # or, as in this case, clicking on the associated label, which is the recommended practice.
    impressive_radio_label = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio_label.click()
    
    # Validate message
    success_message = driver.find_element(By.CSS_SELECTOR, ".mt-3")
    assert "Impressive" in success_message.text
