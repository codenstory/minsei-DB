# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

import sys
sys.stdout = open('articles.txt', 'w', -1, 'utf-8')

URL = "https://minor.town/b/minbokworld"
posts = []
for page in range(1, 1333):
    response = requests.get(URL, params = {"p": str(page)})
    soup = BeautifulSoup(response.text, "lxml")
    anchors = soup.findAll("a", {"class": "vrow"})
    for anchor in anchors:
        if not ("notice" in anchor.get("class")):
            print(anchor.findAll("span", {"class": "col-id"})[0].contents[1].contents[0] + '	' + anchor.findAll("span", {"class": "title"})[0].contents[0] + '	' + anchor.findAll("span", {"class": "user-info"})[0].contents[0] + '	' + anchor.findAll("time")[0].contents[0] + '	' + anchor.findAll("span", {"class": "col-view"})[0].contents[0] + '	' + anchor.findAll("span", {"class": "col-rate"})[0].contents[0])
 
