import sys
import datetime as dt

# datedate= '20221223'
# #datedate_YYYYMMDD= dt.datetime.strptime('20221223','%Y-%m-%d')
# datedate_YYYYMMDD= dt.datetime.strptime(datedate, '%Y%m%d').strftime('%Y-%m-%d')
# print(datedate_YYYYMMDD)


i=0
maxNum= 10
j=1
maxNo=7
# srtYMD기준 maxNum까지 하루 증감하면서 date_ls에 append
for i in range(maxNum):
    for j in range(maxNo):
        print(str(i),'-',str(j))