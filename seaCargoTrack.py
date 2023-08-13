from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class msc:
    def __init__(self,bl:str):
        self.bl = bl
        driver = webdriver.Chrome()
        driver.get("https://www.msc.com/en/track-a-shipment")
        driver.find_element(By.ID,'trackingNumber').send_keys(self.bl)
        driver.find_element(By.ID,'trackingNumber').submit()
        time.sleep(6.0)
        ctn = driver.find_elements(By.CLASS_NAME,"msc-flow-tracking__more-button")
        if ctn != 1:
            for each in ctn:
                each.click()
        data = driver.find_elements(By.CLASS_NAME,'data-value')
        ctnNum = []
        dataGlobal = []
        for a in data:
            if len(a.text) == 11 and not " " in a.text:
                ctnNum.append(a.text)
            dataGlobal.append(a.text)
        
        for i in ctnNum:
            if i in dataGlobal:
                for _ in range(3):
                    dataGlobal.pop(dataGlobal.index(i)+1)
                dataGlobal.pop(dataGlobal.index(i))
        
        print(dataGlobal)
msc('MEDUUJ567731')