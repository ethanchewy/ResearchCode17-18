"""
Graphs Tweets as a Time Series
"""

%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from urllib2 import Request, urlopen
import json

#Read JSON file as a panda's dataframe
jsonFile = "DiscordSentTweets.json"
df = pd.read_json(jsonFile)

