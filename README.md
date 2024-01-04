#Automatisación de descarga de archivo Zip con selenium.

#El archivo extraction.py posee la funcion para automatizar el ingreso hasta el boton de descarga.

#El archivo main realiza una automatización que ingresa a la página https://cde.ucr.cjis.gov/LATEST/webapp/ y realiza la selección de la tabla víctimas en florida dentro de "Documents & Downloads" utilizando el módulo extraction.py, dentro del ZIP se busca el archivo Victims_Age_by_Offense_Category_2022.xlsx. Luego con pandas realiza un limpiado de datos y posteriormente se guarda en un csv.

#Para mejorar el script se podría agregar 2 parámetros con las listas de los estados y las tablas, de esa manera se podrían buscar los ids de cada uno y descargar cualquier tabla deseada.
