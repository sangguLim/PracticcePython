import pandas as pd
import numpy as np

PATH = 'D:\\Barra\\daily\\'

#print(pd.read_csv(PATH+'USA_XSEDOL_Asset_ID_20221216.csv', sep=('|')))

DF_COL_NAME=['datadate','BarraId', 'AssetIDType', 'AssetID','StartDate','EndDate']
# 컬럼명 설정해서 불러오기
data_result = pd.read_csv(PATH+'USA_XSEDOL_Asset_ID_20221216.csv'
                            , sep=('|')
                            ,header=0
                            ,skiprows=1
                            ,skipfooter=1
                            , names = ['Id', 'AssetIDType', 'AssetID','StartDate','EndDate'])
# 단순 행 추가
#data_result['datadate']= '20221216'

# 행 추가 시 옵션 설정
data_result.insert(0,'datadate','20221216')
#new_df= data_result.set_index('BarraId')
#print(new_df)

data_result=data_result['StartDate'=='startdate']
print(data_result)
#df_col_name=[]
# df_col_name=list(data_result.columns)
# print(df_col_name)
# df_col_name.remove('datadate')
# print(df_col_name)
'''
# 특정 문자열 기준 분할
data_result['BarraId']= data_result.Id.str.split(',').str[1]

data_result=data_result[['datadate','BarraId','AssetIDType','AssetID','StartDate','EndDate']]

print(data_result)


# df dtype 조회
#print(data_result.dtypes)
"""
datadate       object
BarraId        object
AssetIDType    object
AssetID        object
StartDate       int64
EndDate         int64
"""
# df 전체 정보 조회
# 실수는 float64, 정수는 int64로 정의 // 그에 따른 메모리는 16.2 mb
#print(data_result.info())
"""
 #   Column       Non-Null Count   Dtype
---  ------       --------------   -----
 0   datadate     352925 non-null  object
 1   BarraId      352925 non-null  object
 2   AssetIDType  352925 non-null  object
 3   AssetID      352925 non-null  object
 4   StartDate    352925 non-null  int64
 5   EndDate      352925 non-null  int64
dtypes: int64(2), object(4)
memory usage: 16.2+ MB
"""


# 컬럼별 min,max check
# 
# for column in data_result.columns:
#     print(column,data_result[column].min(),data_result[column].max())
"""
    datadate 20221216 20221216
    BarraId 1,ARGA591 99999,USA49P1
    AssetIDType CINS LOCALID
    AssetID 000000AKM ZM0000000037
    StartDate 19220718 20221216
    EndDate 19591231 20751231
"""
# df dtype 변경
#data_result.astype({'datadate':'str'})
#data_result['datadate'].astype('str')
#print(data_result.info())

'''