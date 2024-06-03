from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
from fonctions import *

df = pd.read_csv("C:/Users/bruno/Downloads/listing_export_20240530054445.csv", encoding='utf-8', sep=';')

# Chemin vers le driver Selenium (ex: Chrome)
driver_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# URL du site web
url = "https://www.analysetonprod.fr/login/"
echantillon = 'https://www.analysetonprod.fr/dashboard/echantillons/formulaire-analyse'

# Identifiants de connexion

username = pd.read_excel("C:/Users/bruno/Downloads/identifiants.xlsx")['id'][0]
password = pd.read_excel("C:/Users/bruno/Downloads/identifiants.xlsx")['mdp'][0]

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
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "flex")))

    driver.get(echantillon)
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "field_64fb10a27d74d")))

        # Attendre que la connexion soit effectuée (vous pouvez modifier le temps d'attente selon vos besoins)
        for i in df.index:
            
            # Page 1
            input_text(driver, 'field_64fb10a27d74d',df.loc[df.index==i]['Date collecte'].values[0])
            input_text(driver, 'field_64fb10f07d74e',df.loc[df.index==i]['Numero kit'].values[0])
            select_text(driver, 'field_64fb110e7d74f',df.loc[df.index==i]['Cadre collecte'].values[0])
            select_text(driver, 'field_64fb12edd9813', 1)
            select_text(driver, 'field_64fb131ad9814',df.loc[df.index==i]['ID departement'].values[0])
            select_text(driver, 'field_64fb116c7d750',df.loc[df.index==i]['ID de la structure'].values[0])

            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(0.5)
            
            # Page 2
            select_text(driver, 'field_64feda2025464',df.loc[df.index==i]['Sexe usager'].values[0])            
            input_text(driver, 'field_64fedace25465',df.loc[df.index==i]['Age'].values[0])
            input_text(driver, 'field_64fedb1425466',df.loc[df.index==i]['Pseudo usager'].values[0])

            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(0.5)

            # Page 3
            sleep(2)

            try:
                select_text(driver, 'field_64fedbe641a2e',df.loc[df.index==i].iloc[0,1:12].sum())
            except Exception as e :
                input_text(driver, 'field_64fedc4941a2f',df.loc[df.index==i]['Produit autre'].values[0])
                pass
            select_text(driver, 'field_64fedc9541a30',df.loc[df.index==i]['Galenique'].values[0])
            
            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(0.5)
        
            # Page 4
            select_text(driver, 'field_64fee14441a3b',9) # contexte
            select_text(driver, 'field_64feda2025464',df.loc[df.index==i]['id frequence'].values[0]) 
            select_text(driver, 'field_64fede0b41a34',9) # fréquence labo
            select_text(driver, 'field_64fedec041a35',df.loc[df.index==i]['id consomme'].values[0]) 
            try:
                select_text(driver, 'field_64fedf1f41a36',7) # voie de conso
            except:
                pass
            try:                
                select_text(driver, 'field_64fee05941a39',7) # conso envisagée
            except:
                pass
            # TODO: fonction multi selecte
            motif = df.loc[df.index==i].iloc[0,56:62].tolist()
            motif = [x for x in motif if not pd.isna(x)]
            select_multi(driver,'field_64fee09741a3a',motif)     
            
            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(0.5)
            
            select_text(driver, 'field_64ff0c7383dd1',2)
            select_text(driver, 'field_64ff0cb783dd2',3)

            sleep(5)
            
            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(0.5)
            
            # Page 5
            select_text(driver, 'field_64ff0d7483dd5',2) # effet ressenti
            input_text(driver,"field_64ff0e5583dd8",100) # teneur estimé
            select_text(driver,'field_64ff0e8683dd9',1) # unité
            try:
                input_text(driver,'field_64ff0f1483dda','') # effet resenti
            except:
                pass
            input_text(driver,"field_64ff0dac83dd6",100) # teneur vendeur
            select_text(driver,'field_64ff0ddf83dd7',1) # unité
            sleep(10)
            # Page suivante
            next_button = driver.find_elements(By.TAG_NAME, "button")
            next_button[1].click()
            sleep(10)
            
        sleep(50)

        # Fermer le navigateur
        driver.quit()
    except Exception as e :
        print(e)

except Exception as e :
        print(e)