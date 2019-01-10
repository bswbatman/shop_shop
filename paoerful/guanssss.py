import requests
from bs4 import BeautifulSoup
from lxml import etree


taxCode = 4016999090

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Upgrade-Insecure-Requests': '1', 'Host': 'www.hscode.net'
}
pao = requests.get('http://www.hscode.net/IntegrateQueries/QueryYS?tdsourcetag=s_pctim_aiomsg', headers=head)

sesson_id = pao.cookies['ASP.NET_SessionId']

head2 = {
    'Cookie': 'ASP.NET_SessionId=%s' % sesson_id,
    'Host': 'www.hscode.net',
    'Origin': 'http://www.hscode.net',
    'Referer': 'http://www.hscode.net/IntegrateQueries/QueryYS?tdsourcetag=s_pctim_aiomsg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {'pageIndex': '1',
        'taxCode': '%s' % taxCode,
        'productName:': ''
        }
paopao = requests.post('http://www.hscode.net/IntegrateQueries/YsInfoPager',data=data,headers = head2).text

# print(paopao)
html = etree.HTML(paopao)

# bs = BeautifulSoup(paopao,'lxml')
# tax = bs.find_all('div','row_0')
# print('bs4',tax)

lxmll = html.xpath('//*[@class="scx_listitem_0"]/div/div[3]/div[2]//text()')[0]     #/div[1]/div/div[3]//text()')
lx = lxmll.replace('\r','').replace('\n','').strip()
print('lxml',lx)  # best tax