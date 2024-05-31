from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chemin vers le driver Selenium (ex: Chrome)
driver_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# URL du site web
url = "https://www.analysetonprod.fr/login/"
echantillon = 'https://www.analysetonprod.fr/dashboard/echantillons'

# Identifiants de connexion
username = "b.maurin"
password = "4ksh0izcasgr"

# Configuration du navigateur
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")  # Désactiver l'accélération matérielle
options.add_argument("--disable-dev-shm-usage")  # Désactiver l'utilisation de /dev/shm
options.add_argument('--blink-settings=imagesEnabled=false') # this will disable image loading
driver = webdriver.Chrome(options=options)

# Accéder à la page de connexion
driver.get(url)

# Remplir les champs de connexion et soumettre le formulaire
username_field = driver.find_element(By.ID,"user_login")  
password_field = driver.find_element(By.ID, "user_pass")  
submit_button = driver.find_element(By.ID,"wp-submit")  

# Envoyer les données 
username_field.send_keys(username)
password_field.send_keys(password)
submit_button.click()

# Attendre le chargement de la page
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "page-trajet-button")))

    driver.get(echantillon)
    # Attendre que la connexion soit effectuée (vous pouvez modifier le temps d'attente selon vos besoins)
    time.sleep(5)

    # Fermer le navigateur
    driver.quit()

except:
    pass