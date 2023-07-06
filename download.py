#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   实现文件下载,显示下载进度

import os
import requests
import time
# import sys


def download_file(url, store_path="", chunk_size=512):
    filename = url.split("/")[-1]
    save_path = os.path.join(store_path, filename)
    with requests.get(url, stream=True, headers={'Proxy-Connection':'keep-alive'}) as fget:
        file_size = int(fget.headers["Content-Length"])
        print('-' * 32)
        print(f"文件名: {save_path}")
        print(f"大小: {file_size/(1000**2)}Mb")
        print(f"地址: {url}")
        print('-' * 32)
        # 文件已下载大小
        file_done = 0
        # 上一次前文件已下载大小
        pre_file_done = 0
        # 上一次计算下载速度的时间
        pre_time = time.time()
        # 下载速度
        speed = 0
        with open(save_path, "wb") as fw:
            for chunk in fget.iter_content(chunk_size):
                fw.write(chunk)
                file_done += chunk_size
                percent = file_done / file_size
                t = time.time()
                if t - pre_time > 2: 
                    speed = (file_done - pre_file_done) / 1024 / 1024 / 2
                    pre_file_done = file_done
                    pre_time = t
                if file_done <= file_size:
                    print(f"下载中: {percent:.2%} {speed:.2f}M/S", end='\r')
                else:
                    print("下载完毕: 100%")
        time.sleep(2)
        os.remove(save_path)
        print("删除文件")

def formatFloat(num):
    return '{:.2f}'.format(num)

if __name__ == "__main__":
    # 读取运行指令携带的参数
    # print(str(sys.argv))
    # url = sys.argv[1]
    # path = sys.argv[2]
    # chunk_size = sys.argv[3]
    n = 1
    while 1:
        print(f"第{n}次下载")
        download_file("https://downloads.raspberrypi.org/rpd_x86/images/rpd_x86-2021-01-12/2021-01-11-raspios-buster-i386.iso", "./download")
        n += 1
