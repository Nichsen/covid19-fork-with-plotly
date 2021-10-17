# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:22
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-17 18:03:20
import json
import os
from datetime import datetime

import numpy as np
import plotly
import plotly.graph_objs as go


def genPlotly(): # "dump tool" generationg html form json data creating a simple html from "block code :-/"
    date= datetime.now()
    date = date.strftime("%Y_%m_%d")
    date2 = date
    path ="./Data/"
    calcFile = path + "calc_" + date +".json"
    
    x = []
    y1 = []
    y2 = []
    y3 = []


    with open(calcFile) as file:
        calcData= json.load(file)
        for rows in calcData:
            #rows["Active"] = rows["Confirmed"] - rows["Deaths"] - rows["Recovered"]
            date = str(rows["Date"])
            x.append(date)
            y1.append(rows["Active"])
            y2.append(rows["Confirmed"])
            y3.append(rows["Deaths"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, name="Active", line_shape='linear'))
    """fig.add_trace(go.Scatter(x=x, y=y2, name="Confirmed",
                        text=["tweak line smoothness<br>with 'smoothing' in line object"],
                        hoverinfo='text+name',
                        line_shape='linear'))"""
    fig.add_trace(go.Scatter(x=x, y=y2, name="Confirmed", line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=y3 , name="Deaths", line_shape='linear'))

    fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    fig.show()



