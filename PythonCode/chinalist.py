import urllib.request
import ssl,os,time
from datetime import datetime, timedelta, timezone
context = ssl._create_unverified_context()

#1.hezhijie0327大大白名单url
url = 'https://raw.githubusercontent.com/hezhijie0327/DHDb/master/dhdb_dead.txt'
#2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
#3.构建请求对象
request = urllib.request.Request(url, headers=headers)  #使用Request可以加请求头对象
#4.发送请求对象
response = urllib.request.urlopen(request,context=context)
#5.读取数据
data = response.read()


#6.保存到文件中 验证数据
dirs = './'
if not os.path.exists(dirs):
    os.makedirs(dirs)
with open(dirs+'/cache.txt','wb') as f:
    # print(data)
    f.write(data)
    f.close()

with open(dirs+'/chinalist.txt', 'w+', encoding='utf-8') as f:
    with open(dirs + '/cache.txt', 'r', encoding='utf-8') as cn:
        for line in cn:
            # print(line[:-1])
            instde_dns = 'https://dns.pub/dns-query\n'
            f.write('[/'+line[:-1]+'/]'+instde_dns)
        f.close()
