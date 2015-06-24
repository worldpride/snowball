#snowball

#简介
抓取雪球优异组合的持仓调仓

#运行
运行driver.py程序，查看运行效果


#工作计划：
	1. 环境和工具准备
			i.python环境和IDE的安装
			ii.pip的安装：官网下载安装包，然后运行python setup.py install
			iii. django的安装：使用pip直接安装：  pip install Django==1.8.2
			iv. 数据库的安
			v. fiddler抓包模拟http请求工具
	
	2. 单线程网页爬取某一个组合仓位信息-snowSpider.py
	3. 实现多线程爬取多个组合-threadPool.py
	4. 完成读取配置文件类confRead.py
	5. 建立后台数据库 
	6. 加入日志模块
	7. 实现事件驱动引擎 (当仓位发生变化时触发一系列的回调函数，如何侦测到仓位的变化？没想好)
	8. 多个组合都选中某支股票时--怎样的逻辑?? (暂定)
	9. 界面
