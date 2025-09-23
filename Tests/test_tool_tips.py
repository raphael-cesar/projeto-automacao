from Pages.tool_tips_pages import ToolTipsPage

def test_tool_tips_button(driver, test_data):
    tool_tips_box_page = ToolTipsPage(driver)
    tool_tips_box_page.navigate(test_data["tool_tips_url"])

    tool_tips_box_page.hover_over_button()
    assert tool_tips_box_page.is_hover_tool_tips_button_correct(test_data["tool_tip_button_text"])
    
def test_tool_tips_text_field(driver, test_data):
    tool_tips_box_page = ToolTipsPage(driver)
    tool_tips_box_page.navigate(test_data["tool_tips_url"])

    tool_tips_box_page.hover_over_text_field()
    assert tool_tips_box_page.is_hover_tool_tips_text_field_correct(test_data["tool_tip_field_text"])