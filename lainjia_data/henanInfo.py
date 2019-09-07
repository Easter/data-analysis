import re
from bs4 import BeautifulSoup
import requests
import time
import json

def index_page(page):
    i = 0
    # url = "https://bj.lianjia.com/ershoufang/pg" + str(page) + "lc" + str(floor) + "ea20000ep100000rs%E5%8C%97%E4%BA%AC/"
    # url = "https://bj.lianjia.com/ershoufang/pg" + str(page) + "/"
    url = "https://xinxiang.lianjia.com/ershoufang/changyuanxian/pg" + str(page) + "/"
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }

    result = requests.get(url=url,headers=headers)
    html = result.text
    soup = BeautifulSoup(html,"html.parser")
    results = soup.find_all(attrs={"class":"clear LOGCLICKDATA"})

    for result in results:
        get_info(result)
        i += 1
        print(str(i) + "个")

def get_info(result):
    pattern = "\d+\.?\d*"
    pattern1 = "\d+"
    try:
        houseinfos = result.find("div", "houseInfo").contents[2].split("|")
        court = result.find("div", "houseInfo").contents[1].string.strip()
        floor = result.find("div", "positionInfo").contents[1].split(" ")[0]
        address = result.find("div", "positionInfo").contents[2].string
        decoration = houseinfos[4].strip()
        direction = houseinfos[3].strip().replace(' ', '')
        square1 = houseinfos[2].strip()
        unit_Price = result.find("div", class_="unitPrice").attrs["data-price"]
        total_Price = result.find("div", class_="totalPrice").find("span").string
        square1 = re.findall(pattern=pattern, string=square1)
        # year = result.find("div",class_="positionInfo").cotents[2]
        # year1 = re.findall(pattern=pattern1,string=year)
        roomtype = houseinfos[1].strip()

        if is_number(total_Price):
            information = {
                "court": court,
                "decoration": decoration,
                "square": float(square1[0]),
                "unit_Price": int(float(unit_Price)),
                "total_Price": int(float(total_Price)),
                "roomtype": roomtype,
                "floor": floor,
                "address": address,
                "direction": direction
                # "year":int(year1[0])
            }
            infos.append(information)
        else:
            pass

    except TimeoutError:
        print("超时异常")
        pass

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

if __name__ == '__main__':
    infos = []
    for page in range(1,2):
        i = 0
        print("正在爬取第{}页".format(page))
        index_page(page=page)
        time.sleep(3)

    jsObj = json.dumps(infos,ensure_ascii=False,indent=4)
    # fileObject = open('新乡.json', 'w')
    # fileObject = open("河南\新乡\新乡.json","w",encoding="utf-8")
    # fileObject = open("test.json","w",encoding="utf-8")
    fileObject = open("河南\新乡\长垣县\长垣县.json", "w", encoding="utf-8")
    fileObject.write(jsObj)
    fileObject.close()
    for i in range(1,100):
        print(i)
