#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 单线程
# directory_scan

import requests
import sys  # 和系统产生交互

url = sys.argv[1]  # 获取输入的第一个参数
dit = sys.argv[2]  # 获取字典文件
headers = {
    'User-Agent': 'https://minipc.eastday.com/ecms/thumbimg/20230129/893x487_63d6182c505d2_mwpm_03200403.jpeg?qid=02157'}

# url=str(input('Please enter the url:'))#自己输入目标url
with open(dit, 'r') as f:
    # with open('directory_list.txt','r') as f:
    for line in f.readlines():
        line = line.strip()
        r = requests.get(url + "/" + line, headers=headers)
        if r.status_code == 200:
            print('URL:' + r.url)
            print(r.request.headers)

