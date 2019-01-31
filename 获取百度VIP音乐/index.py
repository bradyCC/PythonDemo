# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 9:43
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests
import re
import json
import os


# 获取音乐ID
def getSongId(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        mids = re.findall(r'sid&quot;:(\d+)', html)
        return mids
    except IOError:
        print('爬取失败')


# 根据音乐ID获取音乐详情
def getMusicUrl(mids):
    try:
        data = []
        apiUrl = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery17206453751179783578_1544942124991&songid={mid}&from=web'
        for mid in mids:
            r = requests.get(apiUrl.format(mid=mid))
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            regex = re.compile(r'{.*}')
            data.append(re.findall(regex, r.text))
        return data
    except IOError:
        print('获取失败')


# 保存音乐
def saveMusic(filename, url):
    root = 'E://musics//'
    path = root + filename + '.mp3'
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                print('文件保存成功')
        else:
            print('文件已存在')
    except IOError:
        print('保存失败')


def main():
    url = 'http://music.taihe.com/search?key=林俊杰'
    mid = getSongId(url)
    data = getMusicUrl(mid)
    for item in data:
        saveMusic(json.loads(item[0])['songinfo']['title'], json.loads(item[0])['bitrate']['file_link'])


if __name__ == '__main__':
    main()

