from Pages.elements_pages import ElementsPage
import pytest

def test_navigate_to_elements_page(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert "elements" in driver.current_url

def test_locate_by_id(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_id_displayed()
    assert elements_page.is_check_box_text_correct("Text Box")
@pytest.mark.smoke  
    
def test_locate_by_css_selector(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_css_displayed()
@pytest.mark.smoke
    
def test_locate_by_xpath(driver):
    elements_page = ElementsPage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_xpath_displayed()