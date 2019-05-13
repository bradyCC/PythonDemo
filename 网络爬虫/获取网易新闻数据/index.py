# -*- coding: utf-8 -*-
# @Time    : 2019-02-08 09:20
# @Author  : brady
# @Email   : acheng_@163.com
# @File    : index.py
# @Software: PyCharm

import requests
import re


def get_news_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # response.encoding = response.apparent_encoding
        return response.text
    except IOError:
        print(IOError)


def get_news_list(html):
    newsList = []
    news = re.findall(r'<div class="tabContents">.*?</div>', html, re.S)
    for item in news:
        data = re.findall(r'<a href="(.*?)">(.*?)</a>', item, re.S)
        newsList += data
    return newsList


def save_news_list(newsList):
    for newsItem in newsList:
        news_url = newsItem[0]
        news_title = newsItem[1]
        with open('网易新闻数据.txt', 'a') as f:
            f.write(news_url + ' ')
            f.write(news_title + '\n')
            f.close()


if __name__ == '__main__':
    url = 'http://news.163.com/rank/'
    html = get_news_data(url)
    newsList = get_news_list(html)
    save_news_list(newsList)


