import re
import json

pattern = "\d+"
educates = ["大专","本科","硕士"]
def index(educate):
    salary_avgs = []
    with open("{}.json".format(educate),"r") as jf:
        salaryavg_list = []
        results = json.load(jf)
        for result in results:
            salary = result["salary"]
            salary1 = re.findall(pattern=pattern,string=salary)
            print(salary1)
            salary_avg = int((int(salary1[0]) + int(salary1[1]))/2)
            salaryavg_list.append(salary_avg)
    salary_avgs += salaryavg_list
    return salary_avgs

def save_avg(list,educate):
    jsObj = json.dumps(list,ensure_ascii=False)
    fileObject = open('{}平均.json'.format(educate), 'w')
    fileObject.write(jsObj)
    fileObject.close()


if __name__ == '__main__':
    for educate in educates:
        list = index(educate=educate)
        save_avg(list=list,educate=educate)