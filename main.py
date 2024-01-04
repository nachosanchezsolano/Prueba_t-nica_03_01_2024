from zipfile import ZipFile
import pandas as pd
from extraction import extraction_with_firefox

url="https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home"

path=["//a[@id='hr-docs-icon-action']",
      "//*[@id='dwnnibrs-download-select']/button",
      "//*[@id='nb-option-71']",
      "//*[@id='dwnnibrsloc-select']/button",
      "//*[@id='nb-option-97']",
      "//*[@id='nibrs-download-button']"]

download_time=3

extraction_with_firefox(url=url,paths=path,sleep_time=3)

with ZipFile('victims.zip', 'r') as file:
    with file.open("Victims_Age_by_Offense_Category_2022.xlsx") as excel_file:
        df = pd.read_excel(excel_file)

df = df.iloc[:-1]
df = df[(df['Victims'] != 'Total') & (df['Victims'] != 'Crimes Against Persons') & (df['Victims'] != 'Crimes Against Property')]
print(df)
df.to_csv("Victims_Age_by_Offense_Category_2022.csv", index=False)
