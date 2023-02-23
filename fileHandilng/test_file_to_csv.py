# 작성일: 2022-12-22
# 작성자: 임상구
# 내용: convert to csv file from other type file (everyday)


from pathlib import Path
import pandas as pd
import datetime as dt

def replace_point(file_nm):
    result = file_nm.replace(".","_")
    return result

# 날짜 설정 (보통 전일자 데이터는 다음날 오후 3시~4시 사이에 적재됨)
# yesterday='221221'
# yesterday_YYYYMMDD= '20221216'
yesterday= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%y%m%d') 
yesterday_YYYYMMDD= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%Y%m%d') 
# yesterday_YYYYBDD= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%Y%b%d')     #e.g.2022Dec20

# zip file
# raw data repository
PATH= 'D:\\Barra\\dailyZipuncompress\\'
# save repository
SAVE_PATH = 'D:\\Barra\\daily\\'

# dailyZipuncompress
file_ls = [
    'FP_USMEDS_Factor_POR',             
    'USA_Asset_ID',                     #일단위 소급안됨(22/12/16~)
    'USA_Asset_Identity',               
    'USA_LOCALID_Asset_ID',              #일단위 소급안됨(22/12/16~)
    'USA_XSEDOL_Asset_ID',              
    'USMED_100_Asset_Descriptor',       
    'USMED_100_Asset_DlySpecRet',       
    'USMED_100_Asset_Std_Descriptor',   
    'USMED_100_Descriptors.dat',        #.dat
    'USMED_Daily_Asset_Price',          
    'USMED_ESTU_POR',                   
    'USMED_Market_Data',                
    'USMED_Rates',                      
    'USMEDS_100_Asset_Data',          
    'USMEDS_100_Asset_Exposure',      
    'USMEDS_100_Asset_LSR',             
    'USMEDS_100_Asset_PrecisionExposure',       #일단위 소급안됨(22/12/16~)
    'USMEDS_100_Asset_UnadjSpecificRisk',       
    'USMEDS_100_Covariance',            
    'USMEDS_100_DlyFacRet',             
    'USMEDS_100_preVRACovariance',      
    'USMEDS_100_UnadjCovariance',       
    'USMEDS_ETF_100_Asset_Data',        
    'USMEDS_ETF_100_Asset_Exposure'     
]
file_nm= 'USA_XSEDOL_Asset_ID'


# csv 변환 시작
# for i in file_ls:
#     try:
#         if i == 'USMED_100_Descriptors.dat':
#             txtfile_nm=i
#             csvfile_nm = i.replace('.dat','')
#             # text file 읽어오기
#             file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#             # csv file 읽어오기
#             new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")
#         else:
#             # USA_XSEDOL_Asset_ID.221221
#             txtfile_nm= i+'.'+yesterday_YYYYMMDD
#             csvfile_nm= i+'_'+yesterday_YYYYMMDD
#             # text file 읽어오기
#             file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#             # csv file 읽어오기
#             new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")
#     except Exception as e:
#         #print(e)
#         continue


#개별 변환
txtfile_nm= file_nm+'.'+yesterday_YYYYMMDD
csvfile_nm= file_nm+'_'+yesterday_YYYYMMDD
# text file 읽어오기
file = pd.read_csv(PATH + txtfile_nm)
# csv file 읽어오기
new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")



# Barra\\dailyZip\\daily
PATH= 'D:\\Barra\\dailyZip\\daily\\'
SAVE_PATH = 'D:\\Barra\\daily\\'

file_ls= [
    'USMED',                    # .RATE .ESTU .DFRT
    'USMEDS',                   # .COVU .COVV .COV
    'USMEDS_LOCALID',           # .BET .RSK .LSR
    'USMED_LOCALID'            # .IDS .DSRT .DRET           
]

usmedType_ls= [
    '.RATE',
    '.ESTU',
    '.DFRT'
]
usmedsType_ls= [
    '.COVU',
    '.COVV',
    '.COV'
]

slocalidType_ls=[
    '.BET',
    '.RSK',
    '.LSR'
]
localidType_ls=[
    '.IDS',
    '.DSRT',
    '.DRET'
]

# for i in file_ls:
#     try:
#         if i == 'USMEDS':
#             for j in usmedsType_ls:
#                 txtfile_nm=i+yesterday+j
#                 csvfile_nm = txtfile_nm.replace('.','_')
#                 # text file 읽어오기
#                 file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#                 # csv file 읽어오기
#                 new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")

#         elif i == 'USMED':
#             for j in usmedType_ls:
#                 txtfile_nm=i+yesterday+j
#                 csvfile_nm = txtfile_nm.replace('.','_')
#                 # text file 읽어오기
#                 file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#                 # csv file 읽어오기
#                 new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")
#         elif i == 'USMED_LOCALID':
#             for j in localidType_ls:
#                 txtfile_nm=i+'_'+yesterday+j
#                 csvfile_nm = txtfile_nm.replace('.','_')
#                 # text file 읽어오기
#                 file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#                 # csv file 읽어오기
#                 new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")
#         else:
#             for j in slocalidType_ls:
#                 txtfile_nm=i+'_'+yesterday+j
#                 csvfile_nm = txtfile_nm.replace('.','_')
#                 # text file 읽어오기
#                 file = pd.read_csv(PATH + txtfile_nm, low_memory=False)
#                 # csv file 읽어오기
#                 new_csv_file = file.to_csv(SAVE_PATH + csvfile_nm + ".csv")
#     except Exception as e:
#         print(e)
#         continue

"""
# csv file명 설정
replace_file_nm = replace_point(file_nm)

print(PATH + FOLD_PATH + file_nm + ".txt")
print(SAVE_PATH + replace_file_nm + ".csv")

# text file 읽어오기
file = pd.read_csv(PATH + FOLD_PATH + replace_file_nm + ".csv")
# csv file 읽어오기
new_csv_file = file.to_csv(SAVE_PATH + replace_file_nm + ".csv")

"""

"""
# csv file명 설정
replace_file_nm = replace_point(file_nm)

print(PATH + FOLD_PATH + file_nm + ".txt")
print(SAVE_PATH + replace_file_nm + ".csv")

# text file 읽어오기
file = pd.read_csv(PATH + FOLD_PATH + replace_file_nm + ".csv")
# csv file 읽어오기
new_csv_file = file.to_csv(SAVE_PATH + replace_file_nm + ".csv")
"""