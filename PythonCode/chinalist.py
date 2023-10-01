import urllib.request
import ssl,os,re
from datetime import datetime, timedelta, timezone
def get():
    context = ssl._create_unverified_context()

    #1.mouyase大大白名单url
    url = 'https://raw.githubusercontent.com/xhrzg2017/AdGuard-Home/master/CN.txt'
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
    dns()

def dns():
    dirs = './'
    with open(dirs+'/cache1.txt', 'w+', encoding='utf-8') as file:
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        time = utc_dt.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')
        info = '# ' + time + '更新ChinaList \n'
        file.write(info)
        with open(dirs + '/cache.txt', 'r', encoding='utf-8') as file1:
            for line in file1:
                line=line.replace('\n', '')
                instde_dns = 'https://dns.alidns.com/dns-query\n'
                str1='[/'+line+'/]'+instde_dns
                file.write(str1)
            file.close()
            file1.close()
            os.remove(dirs+'cache.txt')
    clearBlankLine()
#
def clearBlankLine():
    dirs = './'
    with open(dirs+'chinalist.txt', 'w+', encoding='utf-8') as f:
        with open(dirs + 'cache1.txt', 'r', encoding='utf-8') as file2:
            lines = file2.read().split('\n')
            # 删除最后一行
            lines = lines[:-1]
            # 将剩余的行重新写回文件
            f.write('\n'.join(lines))
            f.close()
            file2.close()
            os.remove(dirs + 'cache1.txt')

if __name__ == '__main__':
    get()
