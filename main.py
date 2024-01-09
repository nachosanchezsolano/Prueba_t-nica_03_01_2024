from zipfile import ZipFile
import pandas as pd
from extraction import extraction_with_firefox

"""
Para la ejecución del código es necesario el repositorio completo.
-Con pipy se pueden instalar las dependencias,utilizando el comando "pip install -r requirements.txt".Se recomienda realizarlo en un enviroment aislado.
-De en el repositorio también se encuentran el archivo descargado con el webscraping y el archivo .csv generado para su posterior análisi.

"""

url="https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home"

path=["//a[@id='hr-docs-icon-action']",
      "//*[@id='dwnnibrs-download-select']/button",
      "//*[@id='nb-option-71']",
      "//*[@id='dwnnibrsloc-select']/button",
      "//*[@id='nb-option-97']",
      "//*[@id='nibrs-download-button']"]

download_time=3

"""
La siguiente guncion se encuentra en el módulo extraction.py para una mejor lectura del código.

Posee 3 argumentos:
-url: Es la página por donde se debe comenzar el webscraping, en este código se utiliza https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home
-Paths: Una lista con los Xpaths utilizados para llegar hasta la iunformación necesaria.
-Sleep_time: El tiempo de espera para realizar la descarga, se puede optimizar conociendo el tamaño del archivo.
"""

extraction_with_firefox(url=url,paths=path,sleep_time=download_time)

"""
Utilizando zipfile descomprimimos el archivo descargado y abrimos el xlsx 
con pandas para su limpieza y posteriormente se escribe en archivo .CSV
"""
with ZipFile('victims.zip', 'r') as file:
    with file.open("Victims_Age_by_Offense_Category_2022.xlsx") as excel_file:
        df = pd.read_excel(excel_file)


df = df.iloc[:-1]
df = df[(df['Victims'] != 'Total') & (df['Victims'] != 'Crimes Against Persons') & (df['Victims'] != 'Crimes Against Property')]
print(df)
df.to_csv("Victims_Age_by_Offense_Category_2022.csv", index=False)
