import json
import numpy as np
from pyecharts.charts import Map
from example.commons import Faker
from pyecharts import options as opts

cities = ["新乡","郑州","洛阳","开封","许昌"]
dict = {}
for city in cities:
    unit_Price = []
    with open("河南\{}\{}.json".format(city,city), "r",encoding="utf-8") as jf:
        results = json.load(jf)
        for result in results:
            unitprice = result["unit_Price"]
            unit_Price.append(unitprice)
        arr_mean = np.mean(unit_Price)
    dict[city] = arr_mean
print(dict)

value = list(dict.values()) + [11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480]

attr = ['新乡市', '郑州市', '洛阳市', '开封市', '许昌市'] + ["三门峡市","济源市","焦作市","安阳市","鹤壁市","濮阳市","商丘市","周口市","漯河市",
                                              "驻马店市","信阳市","南阳市","平顶山市"]
# map = Map("河南省房价示例",width=1200,height=600,background_color='#F6CEF5')
# # map.add("",
# #         attr,
# #         value,
# #         maptype='河南',
# #         is_visualmap=True,
# #         visual_text_color='#ff0000',
# #         is_label_show=True,           #是否显示城市名
# #         visual_range=[7500, 16000]
# #         )
map = Map(init_opts=opts.InitOpts(width="900px",height="900px"))
map.add("河南",
        [list(list1) for list1 in zip(attr,value)],
        "河南",
        )
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=7500,max_=16000),title_opts=opts.TitleOpts(title="河南省房价"),toolbox_opts=opts.ToolboxOpts())

map.render("图\河南省房价地图\city_map.html")