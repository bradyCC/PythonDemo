# -*- coding: utf-8 -*-
import scrapy
import json

class CustomerSpider(scrapy.Spider):
    name = 'customer'
    # allowed_domains = ['58shiduoduo.com']
    # start_urls = ['http://test.58shiduoduo.com/crm/html/login']

    # 登录
    def start_requests(self):
        url = 'http://test.58shiduoduo.com/crm/php/hrims/login/login'
        formdata={'username':'SY00001','password':'shangchen@881','user_url':'http://test.58shiduoduo.com/crm/html/login/'}

        # url = 'http://crmapi.58shiduoduo.com/hrims/login/login'
        # formdata = {'username': 'SY00002', 'password': 'qaz123', 'user_url': 'http://crm.58shiduoduo.com/login/'}

        yield scrapy.FormRequest(
            url,
            formdata=formdata,
            callback=self.parse
        )

    draw = 1
    start = 0
    length = 10
    total = 0
    # 获取数据
    def parse(self, response):
        api = response.url
        if api == 'http://test.58shiduoduo.com/crm/php/hrims/login/login':
            token = json.loads(response.text)['data']['token']
        elif api == 'http://test.58shiduoduo.com/crm/php/customer/Customer/getCustomerList':
            token = json.loads(response.text)['token']
            self.total = json.loads(response.text)['recordsTotal']

        url = 'http://test.58shiduoduo.com/crm/php/customer/Customer/getCustomerList'
        formdata={'draw':str(self.draw),'start':str(self.start),'length':str(self.length),'isadmin':'1','token':token}

        # url = 'http://crmapi.58shiduoduo.com/customer/Customer/getCustomerList'
        # formdata = {'draw':'', 'start': '0', 'length': '10', 'isadmin': '1', 'token': token}

        self.start = self.draw * self.length
        self.draw += 1

        if self.total == 0 or self.start < self.total:
            yield scrapy.FormRequest(
                url,
                formdata=formdata,
                callback=self.parse
            )









