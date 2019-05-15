# Python Scrapy

## 常用命令

```python
# 创建一个scrapy项目
# scrapy startproject 项目名

# 生成一个爬虫
# scrapy genspider 爬虫名 爬取网站地址

# 启动爬虫
# scrapy crawl 爬虫名
```

## 相关模块

### logging 模块的使用
- scrapy
  - settings设置LOG_LEVEL = 'WARNING'       # 设置日志显示等级
  - settings设置LOG_FILE = './log.log'      # 设置日志文件保存位置
  - import logging
  - logger = logging.getLogger(__name__)
  - logger.warning()
  
- 普通项目中
  - import logging
  - logging.basicConfig()                   # 设置日志输出的格式和样式
  - logger = logging.getLogger(__name__)    # 实例化logging
  - 在任何py文件中调用logger即可
  
## 变量解析

```python
# 爬虫名Spider文件中
name = 'itcast'                                                     # 爬虫名
allowed_domains = ['itcast.cn']                                     # 允许爬取的范围
start_urls = ['http://www.itcast.cn/channel/teacher.shtml']         # 最开始请求的url地址
```  

## Scrapy Shell - scrapy shell 交互终端

> 命令： scrapy shell http://www.baidu.com

## 创建CrawlSpider 爬虫
> 命令： scrapy genspider -t crawl 爬虫名 爬取地址
