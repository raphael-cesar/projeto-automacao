from Pages.droppable_elements_pages import DroppableElements
from selenium.webdriver.support import expected_conditions as EC

def test_drag_drop(driver):
    dropp_elem = DroppableElements(driver)
    dropp_elem.navigate()
    dropp_elem.drag_drop()