# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:18
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-07 18:51:19

"""
Just a small view to keep covid 19 data in mind ;-)
__author__ = "Nichsen"
__path__ = "https://github.com/Nichsen"
__version__ = "1.0"
__twitter__ = "twitter.com/Nichsen13"
"""
# Main File!
import src_code.analyseData as analyse
import src_code.generatePlotly as PlotlyGen
import src_code.getData as getData

getData.apiCall()  #Create json file for current day
analyse.renderCurrentDay() # Create calc json file
PlotlyGen.genPlotly() #Create Plotly
#filePath = HTMLgenerator.genHtmlfile() # creates html file for current day
#print(filePath) # output of html file



