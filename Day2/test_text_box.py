import time
from selenium.webdriver.common.by import By
def test_fill_text_box(driver):
    driver.get("https://demoqa.com/text-box")
    #Mapeamento dos elementos
    full_name_input = driver.find_element(By.ID, "userName")
    email_input = driver.find_element(By.ID, "userEmail")
    current_address_input = driver.find_element(By.ID, "currentAddress")
    permanent_address_input = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(By.ID, "submit")
    
    #Variaveis de preenchimento dos elementos
    nome = "Rapha"
    email = "rrsm2@cesar.com"
    endereco_atual = "Rua A, 123"
    endereco_permanente = "Rua B, 456"
    
    #Preenchimento dos elementos com as variaveis
    full_name_input.send_keys(nome)
    email_input.send_keys(email)
    current_address_input.send_keys(endereco_atual)
    permanent_address_input.send_keys(endereco_permanente)
    
    #Scroll para o botão submit
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()
    time.sleep(2)  # Espera para garantir que a submissão foi processada
    
    # Map output elements
    output_name = driver.find_element(By.ID, "name")
    output_email = driver.find_element(By.ID, "email")
    output_current_address = driver.find_element(By.CSS_SELECTOR, "p#currentAddress")
    output_permanent_address = driver.find_element(By.CSS_SELECTOR, "p#permanentAddress")

    # Check output
    assert nome in output_name.text
    assert email in output_email.text
    assert endereco_atual in output_current_address.text
    assert endereco_permanente in output_permanent_address.text


    
    