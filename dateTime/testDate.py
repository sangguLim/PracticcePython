import sys
import datetime as dt


#TODAY = dt.datetime.now() + dt.timedelta(days=-12)
#TODAY_YYYYMMDD = TODAY.strftime('%Y-%m-%d')
# .strftime('%Y-%m-%d') # 날짜 형태 변환 함수
# datetime.timedelta(days=-1)   # 날짜 증감 함수
#print(TODAY_YYYYMMDD)

date = '20221024'
srtYMD = '20221024'
endYMD = '20221231'
srtDate= dt.datetime.strptime(srtYMD,'%Y%m%d')
#newDate = dt.datetime.strptime(srtdate,'%Y%m%d')       # '%Y%m%d'는 YYYYMMDD / '%y%m%d'는 YYMMDD
date_ls=[]

print(dt.datetime.now().strftime('%Y%b%d'))

# i=0
# for i in range(i,60):
#     plusDate= srtDate + dt.timedelta(days=i) 
#     YMD=plusDate.strftime('%Y%m%d')
#     #print(plusDate.strftime('%Y%m%d'))
#     date_ls.append(YMD)

# print(date_ls)

#print(newDate)