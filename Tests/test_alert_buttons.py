from Pages.alert_buttons_pages import AlertsButton

def test_alert(driver):
    alerts_button = AlertsButton(driver)
    alerts_button.navigate()
    alerts_button.see_alert("You clicked a button")
    alerts_button.five_seconds_alert("This alert appeared after 5 seconds")
    alerts_button.options_alert_accept("You selected Ok")
    alerts_button.options_alert_dismiss("You selected Cancel")
    alerts_button.input_name_alert("You entered Raphael","Raphael")
        