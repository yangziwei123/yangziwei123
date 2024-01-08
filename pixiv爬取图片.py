import json
import os
import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import random
import urllib.request
from urllib.parse import urlencode

proxies_box = [
    {'http': '117.26.41.218:8888'},
    {'http': '58.220.95.86:9401'},
    {'http': '122.136.212.132:53281'}
]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Referer': 'https://www.pixiv.net/',
    'Cookie': 'first_visit_datetime_pc = 2023 - 11 - 03 % 2009 % 3A43 % 3A29;p_ab_id = 3;p_ab_id_2 = 7;p_ab_d_id = 2098432371;yuid_b = ECWUWUk;_fbp = fb.1.1698972246626.1722899333;PHPSESSID = 94197093_N7wHc7D8caXarADVXgIgKbsrPqASbcr1;c_type = 26;privacy_policy_agreement = 0;privacy_policy_notification = 0;a_type = 0;b_type = 1;login_ever = yes;_gcl_au = 1.1.773504433.1698972300;_im_vid = 01HE9A9JMVJTCQCXGHPGCP8YMT;__utmv = 235335808. | 2 = login % 20ever = yes = 1 ^ 3 = plan = normal = 1 ^ 5 = gender = male = 1 ^ 6 = user_id = 94197093 = 1 ^ 9 = p_ab_id = 3 = 1 ^ 10 = p_ab_id_2 = 7 = 1 ^ 11 = lang = zh = 1;_ga_1Q464JT0V2 = GS1.1.1698972800.1.0.1698972814.46.0.0;__utmz = 235335808.1701137319.2.2.utmcsr = index.jitsu.top | utmccn = (referral) | utmcmd = referral | utmcct = /; __utmc = 235335808;QSI_S_ZN_5hF4My7Ad6VNNAi = v:0: 0;_gid = GA1.2.1880946221.1701835728;__utma = 235335808.49327128.1698972242.1701836150.1701845123.7;cto_bundle = HewlVl9jRHk5JTJGRTBIcnlLem9ZTFl0T3AwT1NERkRXQzhSZ1RyejlXYnJrN0IxcWR0Y2sxMWZoTWl2QklWM3I5enlJbzRqaDVFM0oyM2lGWHprZXNDd2loeTFOOVhGUCUyRjdnREc1RUE4ckdYM3Q4eGxDclBrTk9oU2RrSVhuNnFsZUV6M2NzUXBSQUpXdiUyRnJiM1k5N2QlMkJTYTR0ZyUzRCUzRA;cf_clearance = o2H1T00358o0yNMuqR3lkw.DNPH.YdyfxX0sLg2nB6Y - 1701862093 - 0 - 1 - 2c52b6df.59bd9ce0.7b53e93f - 0.2.1701862093;__utmb = 235335808.17.10.1701848619;_ga_75BBYNYN9J = GS1.1.1701861191.8.1.1701862167.0.0.0;_ga = GA1.2.49327128.1698972242;__cf_bm = 7nwGeNpVNm3NCU1Lykx65_TrWQLmw478o0Bs9aPFnhk - 1701862455 - 0 -'
}


def get_url(page):
    payload = {
        'word': '原神',
        'order': 'date_d',
        'mode': 'all',
        'p': page,
        'csw': '0',
        's_mode': 's_tag',
        'type': 'all',

        'lang': 'zh',
        'version': '7a6bad4fc7fafe7c7cfbae27595883a0fb8be947'
    }
    url = 'https://www.pixiv.net/ajax/search/artworks/%E5%8E%9F%E7%A5%9E?' + urlencode(payload)
    print(url)
    try:
        proxies = random.choice(proxies_box)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_img_url(url, page):
    ys = f"page{page}"  # 创建一个新的文件夹
    for a in range(0, 60):  # 修改这里的范围
        url_value = url.get("body", {}).get("illustManga", {}).get("data", [{}])[a].get("url", None)  # 获取url
        modified_url = url_value.replace("/c/250x250_80_a2", "")  # 裁剪url
        url_id = url.get("body", {}).get("illustManga", {}).get("data", [{}])[a].get("id", None)  # 获取id
        filename = os.path.join(r'C:\Users\yangziwei\Desktop\123', ys, f"{os.path.basename(url_id)}.jpg")
        os.makedirs(os.path.dirname(filename), exist_ok=True)  # 创建文件夹，如果已存在则忽略
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = requests.get(modified_url, headers=headers, verify=False)
        res.raise_for_status()  # 检查是否有错误
        with open(filename, 'wb') as f:
            f.write(res.content)


if __name__ == '__main__':
    for a in range(1, 30):
        url = get_url(a)
        get_img_url(url, a)

