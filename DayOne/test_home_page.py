from selenium import webdriver

def test_verify_demoqa_title():
    driver = webdriver.Chrome()
        
    driver.get("https://demoqa.com/")
    
    assert "DEMOQA" in driver.title
    
    driver.quit()