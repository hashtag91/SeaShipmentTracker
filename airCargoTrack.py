from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import SST_Gui
from datetime import datetime
result = []
class ethiopian:
    def __init__(self,awb:str):
        self.awb = awb
        url = f"https://cargo.ethiopianairlines.com/e-cargo/cargotrack?awbnumber={self.awb}"
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(option)
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME,'details-control')
        origin = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/table[1]/tbody/tr/td[1]")
        infos = []
        for i in elements:
            i.click()
            elementSingle = driver.find_elements(By.CSS_SELECTOR,'td')
            infos.extend(a.text for a in elementSingle)
        infoSorting = infos[-10:]
        infoSortedUp = infoSorting[:6]
        infoSortedDown = infoSorting[-2:]
        result.extend(iter(infoSortedUp))
        result.extend(iter(infoSortedDown))
        dateSplte = list(infoSortedUp[3])
        dateInfo = {
            'date': "".join(dateSplte[:2]),
            'month': "".join(dateSplte[2:5]),
            'year': "".join(dateSplte[5:7]),
        }
        month = {'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
        today = datetime.now().strftime('%y-%m-%d')
        obtainedDate = datetime(
            int(f"20{dateInfo['year']}"),
            month[dateInfo['month']],
            int(dateInfo['date']),
        ).strftime('%y-%m-%d')
        comp = today >= obtainedDate
        result.append(comp)
        result[0] = origin.text
    def resultFonction():
        return result