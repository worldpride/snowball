# -*- coding:utf-8 -*-  
import confRead

#conf path
config_file_path = 'conf.ini'

#define default golobal parameters
ZHcode_list = [] #定义一个空的组合列表
mainURL = 'http://xuemainu.com/p/' #默认主URL
num_of_threads = 2 #默认设置两个工作线程

mainURL = confRead.read_config(config_file_path, 'URL', 'mainURL')
num_of_threads = int(confRead.read_config(config_file_path, 'NUM_OF_THREADS', 'num_of_threads')) 
ZHcode_list = confRead.read_config(config_file_path, 'ZHcode', 'zhcode').split(',')

def test():
   print "test beginning..."
   print mainURL,num_of_threads,ZHcode_list

if __name__ == '__main__':
    test()
