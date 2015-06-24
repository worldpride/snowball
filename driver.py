# -*- coding:utf-8 -*- 
import socket
import threadPool
import snowSpider
import golobal_parameters


def test_job(mainUrl,zhcode): 
    try: 
        snowSpider.get_portfolio(mainUrl,zhcode) 
    except: 
        print'[%4d]'% zhcode, sys.exc_info()[:2] 
    return  zhcode 
   
if __name__ == '__main__': 
    socket.setdefaulttimeout(10) 
    print'start working...' 
    wm = threadPool.WorkerManager(golobal_parameters.num_of_threads) #初始化线程数
    for zhcode in golobal_parameters.ZHcode_list:
        wm.add_job(test_job,golobal_parameters.mainURL,zhcode) 
    wm.start() 
    wm.wait_for_complete()	

