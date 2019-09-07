import time
import json
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser,20)
infos = []
MAX_PAGE = 30
def index_page(job,educate,page,jobyear):
    # 先爬取第一页再爬取后面的一直点下一页利用for循环
    try:
        print("正在爬取第1页")
        url = "https://www.lagou.com/jobs/list_" + quote(job) + "?px=default" + "&gj=" + quote(jobyear) + "&xl=" + quote(educate)
        browser.get(url)
        get_information(educate)
        # 先爬取前三页实验一下
        for i in range(2,page+1):
            print("正在爬取第{}页".format(i))
            #等待下一页可以点击的时候再点击
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'div.item_con_pager div.pager_container > span.pager_next'))
            )
            submit.click()
            time.sleep(8)
            # 等待数据的节点显示出来再调用get_information()函数
            get_information(educate)
    except TimeoutException: # 捕获超出事件异常，从头开始爬取，后续改进
        index_page(job=job,educate=educate,page=page,jobyear=jobyear)

def get_information(educate):
    # 获得数据，公司名和薪资...或者其他的信息
    html = browser.page_source
    # 利用 pyquery CSS选择器
    doc = pq(html)
    items = doc("div#s_position_list .item_con_list li").items()
    for item in items:
        position = item.find("div.position .position_link span.add em").text()
        information = {
            "companyName":item.attr("data-company"),
            "salary":item.attr("data-salary"),
            "position":position
        }
        print(information)
        infos.append(information)
    jsObj = json.dumps(infos,ensure_ascii=False,indent=4)
    fileObject = open('file.json'.format(educate),'w')
    fileObject.write(jsObj)
    fileObject.close()
# 主函数进行执行
if __name__ == '__main__':
    index_page(job="python工程师",educate="大专",page=MAX_PAGE,jobyear="3-5年")
    # 爬取结束后关闭browser
    browser.close()




