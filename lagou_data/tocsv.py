import csv
import json
import pandas as pd
# educate = ["大专","本科","硕士"]
# for i in educate:
#     with open("{}.json".format(i),"r") as jf:
#         with open("{}.csv".format(i),"w",newline="") as cf:
#             writer = csv.writer(cf)
#             writer.writerow(["companyName","salary","position"])
#             result = json.load(jf)
#             for i in result:
#                 writer.writerow(i.values())
educates = ["大专","本科","硕士"]
for i in educates:
    job_results = []
    with open("{}.json".format(i),"r") as jf:
        results = json.load(jf)
        for result in results:
            job_result = []
            job_result.append(result["companyName"])
            job_result.append(result["salary"])
            job_result.append(result["position"])
            job_results.append(job_result)
    df = pd.DataFrame(data=job_results,
                      columns=['公司全名','薪资','区域'])
    df.to_csv("{}.csv".format(i),index=False,encoding="utf-8")






