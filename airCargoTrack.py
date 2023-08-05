from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import SST_Gui
result = []
class ethiopian:
    def __init__(self,awb):
        self.awb = awb
        url = f"https://cargo.ethiopianairlines.com/e-cargo/cargotrack?awbnumber={self.awb}"
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        info = ['Origin','Destination','Pieces','Volume','AWB','Weight']
        ItemsXPath = ['/html/body/div[4]/div[2]/table[1]/tbody/tr/td[1]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[2]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[3]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[4]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[5]','/html/body/div[4]/div[2]/table[1]/tbody/tr/td[6]']
        for infoCompt, XPath in enumerate(ItemsXPath):
            data = driver.find_element(By.XPATH,XPath)
            result.append(f"{data.text}")
    def resultFonction():
        return result