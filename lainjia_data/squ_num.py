import json
from matplotlib import pyplot as plt

with open("河南\新乡\新乡.json","r") as jf:
    results = json.load(jf)
    dict = {}
    for result in results:
        square = result["square"]
        if int(square) not in dict.keys():
            dict[int(square)] = 1
        else:
            dict[int(square)] += 1
squares = list(dict.keys())

numbers = list(dict.values())

plt.rcParams['font.sans-serif']=['SimHei']
fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax1.plot(years,numbers,alpha=0.6)
ax1.scatter(squares,numbers)
ax1.set_title("面积/数量散点图")
plt.xlabel("面积")
plt.ylabel("数量")
plt.savefig("图\散点\squ_num.jpg")
plt.show()
