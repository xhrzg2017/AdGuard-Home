import urllib.request
import ssl,os,re

def get():
    context = ssl._create_unverified_context()

    #1.felixonmars大大白名单url
    url = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf'
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
        with open(dirs + '/cache.txt', 'r', encoding='utf-8') as file1:
            for line in file1:
                str1=re.sub('server=/','',line)
                str2=re.sub('/114.114.114.114','',line)
                instde_dns = 'https://dns.pub/dns-query\n'
                file.write('[/'+str2[:-1]+'/]'+instde_dns)
            file.close()
    clearBlankLine()

def clearBlankLine():
    dirs = './'
    with open(dirs+'/chinalist.txt', 'w+', encoding='utf-8') as f:
        with open(dirs + '/cache1.txt', 'r', encoding='utf-8') as file2:
            lines = file2.read().split('\n')
            # 删除最后一行
            lines = lines[:-1]
            # 将剩余的行重新写回文件
            f.write('\n'.join(lines))
#
if __name__ == '__main__':
    get()
