from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def input_text(driver, id, text):
    """
    Saisit du texte dans un élément de formulaire identifié par son ID en utilisant un pilote de navigateur WebDriver.

    :param driver: Objet WebDriver utilisé pour interagir avec le navigateur.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver
    :param id: L'ID de l'élément de formulaire dans lequel vous souhaitez entrer du texte.
    :type id: str
    :param text: Le texte que vous souhaitez entrer dans l'élément de formulaire.
    :type text: str
    :return: Aucun retour explicite. La fonction agit en saisissant le texte dans l'élément de formulaire spécifié.
    :rtype: None
    :raises NoSuchElementException: Si aucun élément n'est trouvé avec l'ID spécifié.
    """
    input_aera = driver.find_element(By.ID, id)
    input_aera.send_keys(text)
    
def select_text(driver, id, choice):
    """
    Sélectionne une option dans une liste déroulante identifiée par son ID en utilisant un pilote de navigateur WebDriver.

    :param driver: Objet WebDriver utilisé pour interagir avec le navigateur.
    :type driver: selenium.webdriver.remote.webdriver.WebDriver
    :param id: L'ID de la liste déroulante dans laquelle vous souhaitez sélectionner une option.
    :type id: str
    :param choice: L'indice de l'option que vous souhaitez sélectionner dans la liste déroulante.
    :type choice: int
    :return: Aucun retour explicite. La fonction sélectionne l'option spécifiée dans la liste déroulante.
    :rtype: None
    """
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
        
def select_multi(driver, id, choice):
    select_aera = driver.find_element(By.ID, id)
    select_aera.click()
    sleep(0.5)
    for i in choice:
        script = 'document.querySelectorAll("option")[' + str(choice) + '].click()'
        driver.execute_script(script)
        Scroll = False
        sleep(0.5)
    return
            
            