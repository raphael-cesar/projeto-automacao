from Pages.modal_dialogue_pages import ModalDialoguePage
import pytest
from Utils.data_loader import load_json_data

test_data = load_json_data("Data/test_data.json")

@pytest.mark.smoke
def test_small_modal(driver):
    modal_dialogue_page = ModalDialoguePage(driver)
    
    modal_dialogue_page.navigate(test_data["modal_dialogue_url"])
    modal_dialogue_page.click_small_modal_button()
    assert modal_dialogue_page.is_small_modal_displayed()
    
@pytest.mark.smoke
def test_large_modal(driver):
    modal_dialogue_page = ModalDialoguePage(driver)
    
    modal_dialogue_page.navigate(test_data["modal_dialogue_url"])
    modal_dialogue_page.click_large_modal_button()
    assert modal_dialogue_page.is_large_modal_displayed(test_data["modal_large_text"])