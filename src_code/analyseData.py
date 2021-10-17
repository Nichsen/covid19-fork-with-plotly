# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:22
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-07 18:47:39
import datetime
import json
import os


def createCalcData(rawFile,calcFile):  # calculate data "Active" from other api data 
    # calc raw data to use data
    with open(rawFile) as file:
        rawData= json.load(file)
    
    for rows in rawData:
        rows["Active"] = rows["Confirmed"] - rows["Deaths"] - rows["Recovered"]
        #print(rows["Active"])

    
    with open(calcFile, 'w') as outfile:
        json.dump(rawData, outfile)

    

def renderCurrentDay(): # data stored until today
    date= datetime.datetime.now()
    date = date.strftime("%Y_%m_%d")
    path ="./Data/"

    if os.path.exists(path) == True: #data to file for this day
        print(path, "existiert.")
        raw = path + "raw_" + date +".json"
        calc = path + "calc_" + date +".json"
        createCalcData(raw, calc)


