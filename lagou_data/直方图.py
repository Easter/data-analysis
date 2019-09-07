#coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt

educates = ["大专","本科","硕士"]

for educate in educates:
    df = pd.read_csv('{}.csv'.format(educate),encoding="utf-8")
    pattern = '\d+'
    df["salary"] = df["薪资"].str.findall(pattern)

    avg_salary = []
    for k in df["salary"]:
        int_list = [int(n) for n in k]
        avg_wage = int_list[0] + (int_list[1] - int_list[0])/4
        avg_salary.append(avg_wage)
    df["月工资"] = avg_salary
    print(df["月工资"])
    print(type(df["月工资"]))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.hist(df["月工资"])
    plt.xlabel("{}工资(千元)".format(educate))
    plt.ylabel("频数")
    plt.title("{}工资直方图".format(educate))
    plt.savefig("{}.jpg".format(educate))
    plt.show()
