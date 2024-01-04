from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import re
import time

def extraction_with_firefox(url,paths,sleep_time):

    """
    Extraccion datos con firefox utilizando selenium.

    Parámetros:
    -url: dirección web en la que se quiere comenzar para ejecutar los pasos para alcanzar la descarga del archivo
    -paths: lista de Xpath que se deben seleccionar para llegar al la descarga deseada en orden específico.
    -sleep_time:Tiempo de descarga especulada del archivo (en segundos)

    """
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.dir",str(pathlib.Path.cwd()))
    firefox_options.set_preference("--headless",False)

                                
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)

    try:
       for path in paths:
            id=re.search(r"'(.*?)'", path)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, id.group(1))))
            
            click_process= driver.find_element(By.XPATH,path)
            click_process.click()
            if path == paths[-1]:
                time.sleep(sleep_time)

    finally:        
        driver.quit()
