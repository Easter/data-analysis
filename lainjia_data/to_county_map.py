import json
import numpy as np
from pyecharts.charts import Map
from example.commons import Faker
from pyecharts import options as opts

counties = ["新乡县","凤泉区","卫滨区","卫辉市","原阳县","红旗区","牧野区","辉县市","长垣县"]
dict = {}
for county in counties:
    unit_Price = []
    with open("河南\新乡\{}\{}.json".format(county,county), "r",encoding="utf-8") as jf:
        results = json.load(jf)
        for result in results:
            unitprice = result["unit_Price"]
            unit_Price.append(unitprice)
        arr_mean = np.mean(unit_Price)
    dict[county] = arr_mean
print(dict)

value = list(dict.values()) #+ [11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480,11480]

attr = counties #+ ["三门峡市","济源市","焦作市","安阳市","鹤壁市","濮阳市","商丘市","周口市","漯河市",
                                              #"驻马店市","信阳市","南阳市","平顶山市"]
# map = Map("河南省房价示例",width=1200,height=600,background_color='#F6CEF5')
# map.add("",
#         attr,
#         value,
#         maptype='河南',
#         is_visualmap=True,
#         visual_text_color='#ff0000',
#         is_label_show=True,           #是否显示城市名
#         visual_range=[7500, 16000]
#         )
map = Map(init_opts=opts.InitOpts(width="900px",height="900px"))
map.add("",
        [list(list1) for list1 in zip(attr,value)],
        maptype="新乡",
        )
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map.set_global_opts(title_opts=opts.TitleOpts(title="新乡市",subtitle="各区县房价对比"),
                    toolbox_opts=opts.ToolboxOpts(),visualmap_opts=opts.VisualMapOpts(min_=5000,max_=9000))

map.render("图\新乡市房价地图\county_map.html")