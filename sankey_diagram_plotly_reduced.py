#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sankey diagram test
I am trying to identify the 'full' weighted reltion of ML (and AI)

@author: alberto marocchino
"""

import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly.graph_objs import *

import os
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

# data
#             0
label  = [  "A.I.",
#                  1                    2                    3
            "Machine Learning", "***", "Maths Modelling",
#               4              5               6                7                  8                 9
            "Supervised", "Unsupervised", "Deep Learning", "Reinforcement", "Transfer Learning", "Regression",
#               10                       11                    12                 13                          14                    15                    16                  17               18               19
            "Fraude Detection", "Recommendation Systems", "Clustering", "Natural Language Processing", "Image Recognition", "Medical Diagnosis", "Statistical Arbitrage", "Forecasting", "Epidemiology","Predictive Maintenance",
#                     20                      21                     22
            "Deterministic Modelling", "Stokastic Modelling","Linear Optimization"]
#           AI            ML                Fradude dete          Recommendation             Clustering                  NLP               image recognition        medical diagn            arbitrage                forecasting          predictive main         epidemiology                                                                                        
source = [ 0, 0, 0,    1,1,1,1,1,1,     4,   5, 6, 7, 8,  9,     4,   5, 6, 7, 8,  9,     4,   5, 6, 7, 8, 9,      4, 5, 6, 7, 8, 9,       4, 5, 6, 7, 8, 9,      4, 5, 6, 7, 8,  9,     4,   5, 6, 7, 8, 9,      4, 5, 6, 7, 8,  9,     4, 5, 6, 7, 8,  9,      4, 5, 6, 7, 8,  9,    3, 3, 3,    21, 21, 21, 21, 21, 21, 21,    20, 20, 20, 20, 20, 20, 20,    22, 22]
target = [ 1, 2, 3,    4,5,6,7,8,9,    10,  10,10,10,10, 10,    11,  11,11,11,11, 11,    12,  12,12,12,12,12,     13,13,13,13,13,13,      14,14,14,14,14,14,     15,15,15,15,15, 15,    16,  16,16,16,16,16,     17,17,17,17,17, 17,    19,19,19,19,19, 19,     18,18,18,18,18, 18,   20,21,22,    10, 11, 12, 15, 16, 17, 18,    10, 11, 12, 15, 16, 17, 18,    11, 18]
value  = [20, 0,20,    6,6,3,1,2,2,   0.8,1.45,.6, 0,.4,.33,   0.8,1.45, 0, 0, 0,.33,   .2,1.45, 0, 0, 0,  0,    0.8, 0,.6, 0, 0, 0,     0.8, 0,.6,.9,.4, 0,    0.8, 0,.6, 0,.4,.33,   0.8,1.45, 0, 0,.4, 0,    0.4, 0,.3,.1,.2,.15,   0.4, 0,.3,.1,.2,.15,   0.2,0.2, 0, 0, 0,.33,    6, 8, 6,   8/7,8/7,8/7,8/7,8/7,8/7,8/7,   6/7,6/7,6/7,6/7,6/7,6/7,6/7,     3,  3]
# data to dict, dict to sankey
link = dict(source = source, target = target, value = value)
node = dict(label = label, pad=50, thickness=5)
data = go.Sankey(link = link, node=node)
# plot
fig = go.Figure(data)
plot(fig)
