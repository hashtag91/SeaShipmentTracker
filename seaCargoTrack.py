from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codepays
import pandas as pd

general = []
class msc:
    def __init__(self,bl:str):
        self.bl = bl
        driver = webdriver.Chrome()
        driver.get("https://www.msc.com/en/track-a-shipment")
        driver.find_element(By.ID,'trackingNumber').send_keys(self.bl)
        driver.find_element(By.ID,'trackingNumber').submit()
        time.sleep(6.0)
        genInfo = driver.find_elements(By.CLASS_NAME,'msc-flow-tracking__details-value')
        ctn = driver.find_elements(By.CLASS_NAME,'data-value')
        ctnButton = driver.find_elements(By.CLASS_NAME,"msc-flow-tracking__more-button")
        generalInfo = [d.text for d in genInfo if d.text != ""]
        types = [t.text for t in ctn if t.text != ""]
        finalType = [
            types[types.index(ftype) + 1]
            for ftype in types
            if len(ftype) == 11 and " " not in ftype]
        if len(ctnButton) != 1:
            for each in ctnButton:
                each.click()
        data = driver.find_elements(By.CLASS_NAME,'data-value')
        ctnNum = [] #
        dataGlobal = []
        for a in data:
            if len(a.text) == 11 and " " not in a.text:
                ctnNum.append(a.text)
            dataGlobal.append(a.text)
        for i in ctnNum:
            if i in dataGlobal:
                for _ in range(3):
                    dataGlobal.pop(dataGlobal.index(i)+1)
        checkPoint = 0
        ctnInfoLot = [] # Without container number
        ctnInfoLot1 = [] # With container number
        for b in ctnNum:
            id1 = dataGlobal.index(ctnNum[checkPoint])
            if checkPoint !=  len(ctnNum)-1:
                id2 = dataGlobal.index(ctnNum[checkPoint + 1])
                ctnInfoLot.append(dataGlobal[id1+1:id2])
                ctnInfoLot1.append(dataGlobal[id1:id2])
                checkPoint += 1
            else:
                ctnInfoLot.append(dataGlobal[id1+1::])
                ctnInfoLot1.append(dataGlobal[id1::])
        ctnInfo = [c[:5] for c in ctnInfoLot]
        origin = generalInfo[1].split(" ")[1]
        destination = generalInfo[3].split(" ")[1]
        general.extend(iter([codepays.codepays[origin], codepays.codepays[destination],generalInfo,finalType,ctnNum,ctnInfo]))
    def getGeneralInfo():
        return general
