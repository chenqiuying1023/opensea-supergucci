import csv

import requests







import time

import numpy as np

import csv
from lxml import etree
import jieba.analyse
import requests
from urllib3.util import url
import pandas
import re
from selenium import webdriver
# import http.cookiejar
# import urllib.request
# from selenium.common.exceptions import TimeoutException
# 引入ActionChains鼠标操作类
# from selenium.webdriver.common.action_chains import ActionChains
# from handledetail import getdata
# import re
import time

# /Users/mokai/Desktop/project/pythonProject3/pc-opensea/infohtml
def save_to_file(file_name, contents):
    file_name = file_name.replace("/", ";")
    file_name += ".html"
    file_name = "./info2html/" + file_name
    print(file_name)
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()



def scroll(driver):
    driver.execute_script("""   
        (function () {   
            var y = document.body.scrollTop;   
            var step = 100;   
            window.scroll(0, y);   


            function f() {   
                if (y < document.body.scrollHeight) {   
                    y += step;   
                    window.scroll(0, y);   
                    setTimeout(f, 50);   
                }  
                else {   
                    window.scroll(0, y);   
                    document.title += "scroll-done";   
                }   
            }   


            setTimeout(f, 1000);   
        })();   
        """)




if __name__ == '__main__':
    print(input("输入"))
    url  = "https://opensea.io/activity?search[chains][0]=ETHEREUM&search[eventTypes][0]=AUCTION_SUCCESSFUL"
    #     # getHtml(url)
    # 声明一个CookieJar对象实例来保存cookie
    # saveCookie(url)
    # getCookie(url)
    # getHtmlWithCookie(url)
    # 定义文件名
    option = webdriver.ChromeOptions()  # 实例化option对象
    # option.add_argument("--headless")  # 给option对象添加无头参数
    # option.binary_location = "\browser\Google\Chrome\Application\chrome.exe"

    driver = webdriver.Chrome('chromedriver',  # 实例化浏览器对象,可以指定chromedriver的路径,不指定的话 默认会去找python解释器的同级目录
                              options=option)  # 实例化浏览器对象的时候 把option对象带进来
    print(9999)

    option.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    option.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')


    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'images': 2,
    #     }
    # }
    # option.add_experimental_option('prefs', prefs)

    # print("设置浏览器宽480、高800显示")
    # driver.set_window_size(480, 80000)

    aa = input("输入")

    csv_reader = csv.reader(open('../csv/aa2a2list2.csv', 'r'))
    i = -1
    arrall = []
    infoAllArr = []
    mapp = {}
    mapp[''] = 1
    for row in csv_reader:
        try:
            arr = []
            i += 1
            print("-------------", i)
            if i <= 0:
                continue


            collection = ""
            path = "http://opensea.io"
            # ?tab=favorites
            # ?tab=bids
            # ?tab=bids_made
            if len(row[0]) > 1:
                collection      = path + row[0] + "?tab=bids"
                print(collection)
                driver.get(collection)
                j  =2
                while j< 4:

                    driver.execute_script("window.scrollBy(0,700)")
                    save_to_file("bidinfo" +str(j)+ "inj" + str(i), driver.page_source)
                    time.sleep(2)
                    j += 1





        except Exception as e:
            print("error", e)
            continue


    # name = ['collection', 'ownerAddrRt' , 'createrAddr' , 'ind1', 'ind2', 'ind3']
    # test = pandas.DataFrame(columns=name, data=arrall)
    # test.to_csv('./csv/infov2-0505.csv', encoding='utf-8')

    # name = ['name', 'collection addrRt', 'collection', "ownerAddrRt", "ownerRz", "viewrt", "fav", "createrAddr",
    #         "createrrt", "alltiomPricrt ", "是否有about", "是否有properties", "是否有levels", "是否有stats", "isList", "listPric",
    #         "isoffer", "isofferP", "salepri"]
    # test = pandas.DataFrame(columns=name, data=infoAllArr)
    # test.to_csv('./csv/infoAllArr.csv', encoding='utf-8')
    # time.sleep(1)
        # //*[@id="J_bottomPage"]/span[1]/a[2]
        # //*[@id="comment-0"]/div/div/div/a[@class="ui-page-curr"]/following-sibling::*[1]
        # /html/body/div[5]/div[2]/div[2]/div[1]/div/div[3]/div/span[1]/a[3]
        # xyy = driver.find_element("xpath" , '//*[@id="J_bottomPage"]/span/a[@class="curr"]/following-sibling::*[1]')
        # print(driver.get_attribute("outerHTML"))
        # print(xyy.text)

        # save_to_file("list" + str(i), driver.page_source)
        # scroll(driver)
        # xyy.
        # xyy.click()






