import urllib.request
import ssl,os,time
from datetime import datetime, timedelta, timezone
context = ssl._create_unverified_context()

#1.mouyase大大白名单url
url = 'https://raw.githubusercontent.com/mouyase/ChinaListForAdGuardHome/gh-pages/ChinaList.txt'
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
#print(data)
#6.保存到文件中 验证数据
dirs = './'
if not os.path.exists(dirs):
    os.makedirs(dirs)
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
time = utc_dt.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')
with open(dirs+'/clash_adgdns.txt'， 'w+', encoding='utf-8') as f:
    # print(data)
    info ='#'+time+'更新 \n' + '#本txt文件由Actions定时生成\n#用于clash分流\n#感谢mouyase大大白名单\n#项目地址：https://github.com/xhrzg2017/AdGuard-Home\n'
    f.write(info)
    dns = '127.0.0.1:7874\n'
    f.write(dns)
    outside = '[/webstatic.hoyoverse.com/]127.0.0.1:7874\n'
    f.write(outside)
    f.close()
with open(dirs+'/clash_adgdns.txt'， 'ab') as f:
    f.write(data)
