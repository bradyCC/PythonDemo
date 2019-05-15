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

## 配置settings设置

```python
# 设置错误日志等级
LOG_LEVEL = 'WARNING'
# 设置错误日志保存文件       
LOG_FILE = './log.log'      
# 设置user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

```

## Scrapy Shell - scrapy shell 交互终端

> 命令： scrapy shell http://www.baidu.com

## 创建CrawlSpider 爬虫

- 注意点：
    - 创建模板命令： scrapy genspider -t crawl 爬虫名 爬取地址
    - parse函数不能定义，这个方法已被CrawlSpider用来实现基础url提取等功能
    - 一个Rule对象接手很多参数， Rule(LinkExtractor(allow=r'/Item'), callback='parse_item', follow=True),
    - 不指定callback函数的请求下，如果follow为True，满足该rule的url还会继续被请求
    - 如果多个Rule都满足某一个url，会从rules中选择第一个满足的进行操作


## 下载中间件的使用

- 定义类
- process_request 处理请求，不需要return
- process_response 处理响应，需要return response
- settings中开启中间件