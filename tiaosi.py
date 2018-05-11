import requests
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def hi(id):
    url = "http://blog.csdn.net/bug_moving/article/details/" + id
    print url
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    html = requests.get(url, headers=hea)

    print html.status_code

def write2file(content):
    filename = "123.txt"
    f = open(filename, 'a')
    f.write(content + '\n')
    f.close()

def visit(urlnum):
    hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    url = 'http://blog.csdn.net/bug_moving/article/list/' + str(urlnum)
    #url = 'http://blog.csdn.net/bug_moving'
    # url = 'http://jp.tingroom.com/yuedu/yd300p/'

    html = requests.get(url, headers=hea)

    html.encoding = 'utf-8'

    title = re.findall('<a href="/bug_moving/article/details/([0-9]*?)">', html.text, re.S)
    for each in title:
        print each
        write2file(each)
        name = re.findall('<a href="/bug_moving/article/details/'+each+'">(.*?)</a>', html.text, re.S)
        for na in name:
            write2file(na)

def setPagelsit():
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    url = 'http://blog.csdn.net/bug_moving'
    # url = 'http://blog.csdn.net/bug_moving'
    # url = 'http://jp.tingroom.com/yuedu/yd300p/'

    html = requests.get(url, headers=hea)

    html.encoding = 'utf-8'

    index = re.findall('<span>([0-9]*?.*?)</span>', html.text, re.S)
    print index[0].strip()[7:9]
    global pagelist
    pagelist = int(index[0].strip()[7:9])

def loopvisit(f, n):  # f repeats n times
    if n > pagelist:
        return
    else:
        f(n)
        loopvisit(f, n + 1)

setPagelsit()
loopvisit(visit,1)