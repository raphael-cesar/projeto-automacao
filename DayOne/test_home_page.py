def test_verify_demoqa_title(driver):
    driver.get("https://demoqa.com/")
    assert "DEMOQA" in driver.title
