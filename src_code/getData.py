# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:22
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-07 18:48:01
import datetime
import json

import requests


#  =========== FUNCTIONS =====
def storeData(data):
    date= datetime.datetime.now()  # actual time stamp
    date = date.strftime("%Y_%m_%d") # time fromated
    path= "./Data/raw_" + date + ".json"  # path for raw data
    #print(path)
    jData= json.loads(data)
    """file = open(path,"w")
    file.write(str(jData))
    file.close()"""
    with open(path, 'w') as outfile:
        json.dump(jData, outfile)

# ===============================================================================================================================================
def apiCall():
    #response = requests.get("https://api.covid19api.com/summary")
    link = "https://api.covid19api.com/country/germany/status/confirmed/live?from=2020-03-01T00:00:00Z&to=2020-04-24T00:00:00Z"  # with example filter
    link = "https://api.covid19api.com/country/germany"
    response = requests.get(link)
    # Print the status code of the response.
    if response.status_code == 200:
        print("Erfolg API abfrage: " + str(response.status_code))
        data = response.content
        storeData(data)
    else:
        print("PROBLEME MIT DER API! " + str(response.status_code))

    #print(response.content)


