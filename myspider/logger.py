# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 9:32
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : logger.py
# @Software: PyCharm

# 普通项目中使用
import logging

# 设置日志的输出样式
logging.basicConfig(
    level=logging.WARNING,
    format='%{levelname}s [%(filename)s:%(lineno)d] : %(message)s - %(asctime)s',
    datefmt='[%d/%b/%Y %H:%M:%S]'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.warning('this is warning message')
    logger.warning('this is warning message 1')
