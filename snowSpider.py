# -*- coding:utf-8 -*-  
import urllib2
import json
import time
import os
import threading
import confRead

#get *.html 
def get_html(url):
    send_headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive',
        'Host':'xueqiu.com',
        'Cookie':r'xxxxxx',
    }
    req = urllib2.Request(url, headers=send_headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    return html    

#filter portfolio info from html
def get_portfolio(mainUrl,code):
    url = mainUrl + code
    #print url
    html = get_html(url)

    pos_start = html.find('SNB.cubeInfo = ') + 15
    pos_end = html.find('SNB.cubePieData')
    data = html[pos_start:pos_end]
    dic = json.loads(data)
    
    print 'portfolio code:',dic['symbol']
    print 'total gain :',dic['total_gain']	
    print 'daily gain :',dic['daily_gain']
    print 'monthly gain :',dic['monthly_gain']
    print 'holdings info:'
    stocks = dic['view_rebalancing']['holdings']
    for a_stock in stocks:
        print '    stock code:', a_stock["stock_symbol"]
        print '    holding weight:', a_stock["weight"]
    print '--------------------------------' 

class ThreadClass(threading.Thread):
    def __init__(self,ZHcode,mainURL):
        threading.Thread.__init__(self)
        self.ZHcode = ZHcode
        self.mainURL = mainURL
        
    def run(self):
        #print"start process: %s" % (self.ZHcode)
        get_portfolio(self.mainURL,self.ZHcode)


def test():
    ZHcode_list = ["ZH149078","ZH230410","ZH000826","ZH228157"]
    mainURL = 'http://xueqiu.com/p/'
    for zhcode in ZHcode_list:
        t=ThreadClass(zhcode,mainURL)
        t.start()
		

if __name__ == '__main__':
    test()


	

		

		
		
