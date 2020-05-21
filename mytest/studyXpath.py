#coding: utf-8


from lxml import etree
from io import StringIO
import requests
import re

htmldoc = requests.get('http://localhost:8080/jforum-2.6.2/user/list.page')
# print(type(htmldoc.content),htmldoc.encoding,type(htmldoc.text))
html = etree.HTML(htmldoc.content)
e = html.xpath('//img[@alt="[Logo]"]')
print(e)