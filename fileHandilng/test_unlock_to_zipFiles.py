
# 작성일: 2022-12-22
# 작성자: 임상구
# 내용: unlock to zip files (date to date)

import zipfile
import datetime as dt

PATH = 'D:\\Barra\\dailyZip\\'
SAVE_PATH = 'D:\\Barra\\dailyZipuncompress\\'


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
# 날짜 설정 (보통 전일자 데이터는 다음날 오후 3시~4시 사이에 적재됨)
yesterday= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%y%m%d') 
yesterday_YYYYMMDD= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%Y%m%d') 
yesterday_YYYYBDD= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%Y%b%d')     #e.g.2022Dec20


# 압축 해제 하기
#i = 'SMD_USMED_LOCALID_ID'     # 순서 조정

for i in file_nm_ls:
    try:
        with zipfile.ZipFile(PATH+ i + '_' + yesterday + '.zip', 'r') as existing_zip:
            existing_zip.extractall(SAVE_PATH)
    except:
        continue
