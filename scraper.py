from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.by import By

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        ## ADD CODE HERE ##
        def scrape():
            
            planets_data = []
            for i in range(1,10):
                soup = BeautifulSoup(browser.page_source,"html.parser")
                for ul_tag in soup.find_all("ul",attrs=("class","exoplanet")):
                    li_tag = ul_tag.find_all("li")
                    temp_list=[]
                    for index,tags in enumerate(li_tag):
                        if index==0:
                            temp_list.append(tags.find_all("a")[0].contents[0])

                        else:
                            try:
                                temp_list.append(tags.contents[0])
                            except:
                                temp_list.append("")
                    planets_data.append(temp_list)
         
        
                browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
                with open("scrap_data.csv","w")as f:
                     csvwriter = csv.writer(f)
                     csvwriter.writerow(headers)
                     csvwriter.writerows(planets_data)

                

        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planets_df = pd.DataFrame(planets_data,columns=headers)
planets_df.to_csv("scrap_data.csv", index = True, index_label = "id")

# Convert to CSV

    


