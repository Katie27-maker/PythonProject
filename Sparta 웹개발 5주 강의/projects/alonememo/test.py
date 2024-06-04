from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/ni/basic.nhn?code=194799'

header = {'User-Agent' : 'M'}