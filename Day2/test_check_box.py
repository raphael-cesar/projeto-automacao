from selenium.webdriver.common.by import By
import time

# def test_check_box(driver):
#     driver.get("https://demoqa.com/checkbox")
#     # Expand the tree
#     expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
#     expand_all_button.click()

#     # Select the checkbox "Notes"
#     notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
#     notes_checkbox.click()
    
#     # Validate if checkbox was ticked
#     notes_input = driver.find_element(By.ID, "tree-node-notes")
#     assert notes_input.is_selected()

def test_check_box(driver):
    driver.get("https://demoqa.com/checkbox")
    # Expand the tree
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()
    time.sleep(2)
    note_commands = driver.find_element(By.XPATH, "//label[@for='tree-node-commands']")
    note_commands.click()
    time.sleep(3)
    # Validate if checkbox was ticked
    commands_input = driver.find_element(By.ID, "tree-node-commands")
    assert commands_input.is_selected()