from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import tldextract
import socket
import time
import os
import sys
from .Sqlinject import Sqlinject
from .msqlscan import mysqluser,mysqldbs
from . import crawler,DNSdomain,eternblue,msqlscan,models
# Create your views here.
def show_index(request):
    return render(request ,  'index.html')
def show_tools(request):
    return render(request , 'tools.html')
def show_ending(request):
    return render(request , 'ending.html')
def show_web(request):
    return render(request,  'web.html')
def show_leak(request):
    return render(request, 'leak.html')
def show_test(request):
    return render(request,'test.html')
url1={}
def web(request):
        ip=request.GET['ip_address']
        print(ip)
        domain=ip
        print(domain)
        global url1
        # key_tmp = tldextract.extract(domain)
        # key = key_tmp.subdomain + '.' + key_tmp.domain + '.' + key_tmp.suffix
        # crawler.spider(key,key,10)
        #正式代码：
        # urlfileopen=open('E://毕业设计//ending//ending//result.txt','r')
        # for url in urlfileopen.readlines():
        #     a=Sqlinject.Sqlinject(url)
        #     a.run()
        # 环境不足测试代码：
        b=Sqlinject(domain)
        print(b)
        b.run()
        sqlopen = open('E://毕业设计//ending//ending//sql.txt', 'r')
        sqlinresult=0
        for sqlin in sqlopen.readlines():

            if sqlin=="char inject!!!!!" :
                sqlinresult=1
            else :
                if sqlin=="num inject!!!!!":
                    sqlinresult=2
                else:
                    sqlinresult=0

        url1={'url':domain,'sqlin':sqlinresult}
        models.URLS.objects.create(**url1)
        i={'finish':sqlinresult}
        return JsonResponse(i)
def leak(request):
        ip=request.GET['ip_address']
        print(ip)
        dns=DNSdomain.dns_zone_tranfer_finder(ip)
        print(dns)
        mysql=os.popen("python E://毕业设计//ending//ending//myApp//msqlscan.py -u %s"%(ip))
        i = open('E:\毕业设计\ending\ending\ok.txt', 'r').readlines()
        short=0
        for a in i:
            print(a)
            if a.find("密码:") > 0:
                short=1
        print(short)
        try:
            heartrec=os.popen("python2 E://毕业设计//ending//ending//myApp//openssltest.py %s" %(ip))
            heart=0
            for i in heartrec:
                print(i.find("1"))
                if i.find("1")==0:
                    heart=1
        except Exception:
            heart=0
        print(heart)
        blue=0

        # bluerec=eternblue.sds('192.168.74.1',ip)
        # for i in bluerec:
        #     if i=="WIN":
        #         blue=1
        blue=0
        i={'urlid':ip,'dns':dns,'short':short,'heart':heart,'blue':blue}
        url={'urlid':ip,'dns':dns,'short':short,'heartbl':heart,'eternalb':blue}
        models.URLS.objects.create(**url)
        print(dns)
        print(short)
        print(heart)
        print(blue)
        return JsonResponse(i)
