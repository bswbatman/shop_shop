bs = BeautifulSoup(html, 'lxml')
b = bs.find_all('div', class_=re.compile('m_mod mm_.*? clearfix'))
# print(b)
# print(b[0].get_text())
# print(b[1].get_text())#kong
# print(b[2].get_text())
# print(b[3].get_text())
# print(b[4].get_text())
# print(b[5].get_text())
# print(b[6].get_text())
# print(b[7].get_text())
# print(b[8].get_text())
# for i in range(len(b)):
#     print(b[i].get_test())
'''13 标题'''
title = test.xpath('//*[@id="content"]/div[2]/h1/text()')
print(title[0])

'''14 图片'''
tupian = test.xpath('//*[@class="m_mod mm_014 clearfix"]/div/div/ul/li[1]/img/@src')[0]
print(tupian)

'''16 分类 '''
#略

'''17 价格'''
jiage = test.xpath('//*[@class="m_mod mm_017 clearfix"]/ul/li/b/text()')[0]
print(jiage)

'''28 params'''
para = test.xpath('//*[@class="m_mod mm_016 clearfix"]/ul//li/text()')
print(para)