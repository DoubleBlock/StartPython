# _*_coding:UTF-8_*_
from urllib import request
from bs4 import BeautifulSoup4 as bs

url= 'http://ac.qq.com/ComicView/index/id/632551/cid/2'
res= request.get(url)
soup= bs(res)gh