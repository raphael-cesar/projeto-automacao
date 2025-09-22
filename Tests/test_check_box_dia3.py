from Pages.check_box_pages import CheckBoxPage

def test_check_box_dia3(driver):
    check_box_page = CheckBoxPage(driver)
    check_box_page.navigate()
    
    check_box_page.expand_all()
    
    check_box_page.select_check_box()

    assert check_box_page.get_selected_element()
