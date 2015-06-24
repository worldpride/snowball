# -*- coding:utf-8 -*-  
#desc: use to read ini  
#
# 支持两种方式，一种是类的形式，一种是函数形式
#---------------------  

import sys,os,time  
import ConfigParser  
  
#函数形式
def read_config(config_file_path, field, key):   
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        result = cf.get(field, key)  
    except:  
        sys.exit(1)  
    return result  
  
def write_config(config_file_path, field, key, value):  
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        cf.set(field, key, value)  
        cf.write(open(config_file_path,'w'))  
    except:  
        sys.exit(1)  
    return True  

#类的形式
class Config:  
    def __init__(self, path):  
        self.path = path  
        self.cf = ConfigParser.ConfigParser()  
        self.cf.read(self.path)  
    def get(self, field, key):  
        result = ""  
        try:  
            result = self.cf.get(field, key)  
        except:  
			print "cannot find the value for: [%s:%s]" % (field,key)
			result = ""
        return result  
		
    def set(self, filed, key, value):  
        try:  
            self.cf.set(field, key, value)  
            cf.write(open(self.path,'w'))  
        except:
			print "write configure failed!"
			return False  
        return True  
              
              
 
#函数形式
def read_config(config_file_path, field, key):   
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        result = cf.get(field, key)  
    except:
        print "cannot find the value for: [%s:%s]" % (field,key)	
        sys.exit(1)  
    return result  
  
def write_config(config_file_path, field, key, value):  
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        cf.set(field, key, value)  
        cf.write(open(config_file_path,'w'))  
    except:  
        sys.exit(1)  
    return True  

if __name__ == "__main__":  
   if len(sys.argv) < 4:  
      sys.exit(1)  
  
   config_file_path = sys.argv[1]   
   field = sys.argv[2]  
   key = sys.argv[3]  
   if len(sys.argv) == 4:  
      print read_config(config_file_path, field, key)  
   else:  
      value = sys.argv[4]  
      write_config(config_file_path, field, key, value)  