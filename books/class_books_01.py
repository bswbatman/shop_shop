from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://www.books.com.tw/products/M010053043'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
r = requests.get(url, headers = head)

bs = BeautifulSoup(r.text,'lxml')

# price = bs.find_all('li','price')[0].text
# print(price)

# pic = bs.find_all('div','')
# print(pic)


#===========================
from lxml import etree
lxm = etree.HTML(r.text)

'''标题'''
title = lxm.xpath('//h1[@itemprop="name"]//text()')[0]
print(title)

'''价格'''
pricee = lxm.xpath('//li[@class="price"]')#('//b[@itemprop]/text()') 打折价格
print(pricee)

'''图片'''
pic  = lxm.xpath('//img[@itemprop="image"]//text()')
print(pic)