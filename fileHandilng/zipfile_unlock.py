
# 작성일: 2022-12-22
# 작성자: 임상구
# 내용: unlock to zip files (date to date)

import zipfile
import datetime as dt

PATH = 'D:\\Barra\\dailyZip\\'
SAVE_PATH = 'D:\\Barra\\dailyZipuncompress\\'
file_nm = 'SMD_USMED_XSEDOL_ID'


# zip파일 리스트
file_nm_ls= ['FPD_USMEDS',
    'SMD_USMED_100_Descriptor',
    'SMD_USMED_100_Std_Descriptor',
    'SMD_USMED_ID',
    'SMD_USMED_LOCALID_ID',
    'SMD_USMED_Market_Data',
    'SMD_USMED_XSEDOL_ID',    
    'SMD_USMEDS_100',
    'SMD_USMEDS_100_ETF',
    'SMD_USMEDS_100_PrecisionExp',
    'SMD_USMEDS_100_UnadjCov'
]

# date 리스트
# baseDate='221024'
# date_ls= [ 
#     '221024',
#     '221025',
#     '221026',
#     '221027',
#     '221028',
#     '221031',
#     '221216',
#     '221219',
#     '221220'
# ]

# 원하는 시작 날짜 기입
srtYMD = '20221024'
# YYYYMMDD 형태에서 datetime형태로 변경
srtDate= dt.datetime.strptime(srtYMD,'%y%m%d')
date_ls=[]

i=0
maxNum= 60
# srtYMD기준 maxNum까지 하루 증감하면서 date_ls에 append
for i in range(i,maxNum):
    plusDate= srtDate + dt.timedelta(days=i) 
    YMD=plusDate.strftime('%y%m%d')
    #print(plusDate.strftime('%Y%m%d'))
    date_ls.append(YMD)

# 압축하기
# jungle_zip = zipfile.ZipFile(PATH+ file_nm + '.zip', 'w')
# jungle_zip.write('C:\\Stories\\Fantasy\\jungle.pdf', compress_type=zipfile.ZIP_DEFLATED)

# 압축 해제 하기
#i = 'SMD_USMED_LOCALID_ID'     # 순서 조정

for i in file_nm_ls:
    for j in date_ls:
        try:
            with zipfile.ZipFile(PATH+ i + '_' + j + '.zip', 'r') as existing_zip:
                existing_zip.extractall(SAVE_PATH)
        except:
            continue



# with zipfile.ZipFile(PATH+ file_nm + '.zip', 'r') as existing_zip:
#     existing_zip.extractall(SAVE_PATH)


#fantasy_zip = zipfile.ZipFile(PATH+ file_nm + '.zip')
#fantasy_zip.extract(file_nm + '.csv', SAVE_PATH)
 
#fantasy_zip.close()