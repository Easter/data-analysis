import json
import numpy as np
from matplotlib import pyplot as plt

educates = ["大专","本科","硕士"]

def average(educate):
    with open("{}平均.json".format(educate),"r") as jf:
        result = json.load(jf)
        print(result)
        arr_mean = np.mean(result)
    return arr_mean

def standard(educate):
    with open("{}平均.json".format(educate),"r") as jf:
        result = json.load(jf)
        arr_std = np.std(result, ddof=1)
        # arr_var = np.var(result)
    return arr_std

if __name__ == '__main__':
    averages = []
    standards = []
    for educate in educates:
        average1 = average(educate)
        averages.append(average1)
    for educate in educates:
        standard1 = standard(educate)
        standards.append(standard1)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # axl.plot(educates,standards,"or-",label=u"标准差")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax1.bar(x=educates,height=averages,width=0.7,label="平均薪资")
    ax2 = ax1.twinx()
    ax2.plot(educates,standards,color="y",label="标准差")
    plt.legend()
    plt.savefig("平均及标准差直方图.jpg")
    plt.show()













