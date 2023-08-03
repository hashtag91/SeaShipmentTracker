from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import SST_Gui

class ethiopian:
    def __init__(self):
        print(SST_Gui.air['Ethiopian'])
        url = "https://cargo.ethiopianairlines.com/e-cargo/cargotrack?awbnumber={}".format(SST_Gui.air['Ethiopian'])
        driver = webdriver.Chrome()
        driver.get(url)
        info = ['Origin','Destination','Pieces','Volume','AWB','Weight']
        infoCompt = 0
        ItemsXPath = ['/html/body/div[4]/div[2]/table[1]/tbody/tr/td[1]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[2]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[3]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[4]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[5]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[6]']
        for XPath in ItemsXPath:
            data = driver.find_element(By.XPATH,XPath)
            print(f"{info[infoCompt]} : {data.text}")
            infoCompt += 1