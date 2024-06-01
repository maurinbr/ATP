from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def input_text(driver, id, text):
    input_aera = driver.find_element(By.ID, id)
    input_aera.send_keys(text)
    
def select_text(driver, id, choice):
    Scroll = True
    while(Scroll):
        try:
            select_aera = driver.find_element(By.ID, id)
            select_aera.click()
            script = 'document.querySelectorAll("#' + str(id) +'")[' + str(choice) + '].click()'
            driver.execute_script(script)
            Scroll = False
        except:
            pass
            