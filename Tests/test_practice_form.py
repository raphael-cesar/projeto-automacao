import pytest
import json
from Pages.practice_form_pages import PracticeFormPage

def load_test_data(path):
    with open(path, 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data("data/practice_form_data.json"))
def test_fill_practice_form(driver, data):
    form_page = PracticeFormPage(driver)
    form_page.navigate()
    form_page.fill_form(data)
    form_page.submit_form()
    assert form_page.check_modal_visible()