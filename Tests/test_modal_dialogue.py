from Pages.modal_dialogue_pages import ModalDialoguePage
import time
import pytest

@pytest.mark.smoke
def test_small_modal(driver, test_data):
    modal_dialogue_page = ModalDialoguePage(driver)
    
    modal_dialogue_page.navigate(test_data["modal_dialogue_url"])
    modal_dialogue_page.click_small_modal_button()
    assert modal_dialogue_page.is_small_modal_displayed()
    
@pytest.mark.smoke
def test_large_modal(driver, test_data):
    modal_dialogue_page = ModalDialoguePage(driver)
    
    modal_dialogue_page.navigate(test_data["modal_dialogue_url"])
    modal_dialogue_page.click_large_modal_button()
    assert modal_dialogue_page.is_large_modal_displayed(test_data["modal_large_text"])
    
