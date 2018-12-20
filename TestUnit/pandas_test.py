# -*- coding: utf-8 -*-
import json
import urllib

from pandas import Series
from pandas import DataFrame
from pandas import read_csv
from bs4 import BeautifulSoup

pids = read_csv("data/pids.csv")

pColumns = ['PID', 'Price']
fColumns = ['PID', 'Feature', 'Property']

pData = DataFrame(columns=pColumns)
fData = DataFrame(columns=fColumns)

for pid in pids.pid:
    pid = str(pid)
    pUrl = ''


