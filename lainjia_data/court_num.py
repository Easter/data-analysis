import json
from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
import numpy as np

with open("河南\新乡\新乡.json", "r", encoding="utf-8") as jf:
    results = json.load(jf)

def data():
    # with open("河南\新乡\新乡.json", "r", encoding="utf-8") as jf:
    #     results = json.load(jf)
    dict = {}
    for result in results:
        court = result["court"]
        if court not in dict.keys():
            dict[court] = 1
        else:
            dict[court] += 1

    keys = list(dict.keys())

    for key in keys:
        if dict[key] <= 10:
            del dict[key]
    keys = list(dict.keys())
    values = list(dict.values())
    c = court_num(keys,values)
    # b = court_pri(keys,values)
    return c
    # return b
def court_num(keys,values):
    c = Bar(init_opts=opts.InitOpts(width="900px",height="900px"))
    c.add_xaxis(keys)
    c.add_yaxis("小区房源数量",values)
    c.set_global_opts(
                title_opts=opts.TitleOpts(title="新乡市",subtitle="小区房源数量"),
                datazoom_opts=opts.DataZoomOpts(),toolbox_opts=opts.ToolboxOpts(is_show=True))

    return c

def court_pri(keys,values1):
    dict = {}
    for result in results:
        if (result["court"] in keys) and result["court"] not in dict.keys():
            dict[result["court"]] = [result["unit_Price"]]
        elif (result["court"] in keys) and result["court"] in dict.keys():
            dict[result["court"]].append(result["unit_Price"])
    keys1 = list(dict.keys())
    values = list(dict.values())
    list1 = []
    for i in range(len(values)):
        arr_mean = np.mean(values[i])
        list1.append(int(arr_mean))
    # print(values)
    # print(keys)
    # print("长度" + str(len(keys)))
    # print(list1)
    # print("长度" + str(len(list1)))
    b = Bar(init_opts=opts.InitOpts(width="900px",height="900px"))
    b.add_xaxis(keys1)
    b.add_yaxis("小区价格",list1)
    # b.add_yaxis("小区房源",values1)
    b.set_global_opts(
                title_opts=opts.TitleOpts(title="新乡市",subtitle="各小区平均价格"),
                datazoom_opts=opts.DataZoomOpts(),toolbox_opts=opts.ToolboxOpts())
    return b

if __name__ == '__main__':
     b = data()
     b.render("图\各个小区价格\community_avg_pri.html")
