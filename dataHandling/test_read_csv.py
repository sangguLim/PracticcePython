import pandas as pd
import numpy as np

PATH = 'C:\\Users\\USER\\Downloads\\'

DF_COL_NAME=['datadate','BarraId', 'AssetIDType', 'AssetID','StartDate','EndDate']
# 컬럼명 설정해서 불러오기
data_result = pd.read_csv(PATH+'superstore_sample.csv'
                            , sep=('')
                            ,header=0
                            ,skiprows=0
                            ,skipfooter=0
                            , names = ['RowId', 'OrderId', 'OrderDate','DeliType','CustomerId','CustomerName','Segment','City','Si_do','Country','Nation','GoodsCode','Category','PayAmt','Qnty','DiscRate','Profit'])
# 단순 행 추가
#data_result['datadate']= '20221216'

# 행 추가 시 옵션 설정
data_result.insert(0,'datadate','20221216')
#new_df= data_result.set_index('BarraId')
#print(new_df)

fields = data_result.index
fields_str = ", ".join(fields)
print(fields_str)

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
# for i in range(len(data_result)):
    # print(data_result.iloc[i])

# values = []
# for v in data_result:
#     if isinstance(v, (int, float, np.floating)):
#         values.append(str(v))
#     elif isinstance(v, pd.Timestamp):
#         values.append("'" + v.strftime("%Y-%m-%d") + "'")
#     elif isinstance(v, str):
#         values.append(f"'{v}'")
#     else:
#         raise ValueError(type(v))
# for i, data_row in data_result.iterrows():
#     #BarraId = data_row['BarraId']
#     class_list.append(data_row[index])
#     print(data_row[0:5])

#df_list= data_result.iloc[1]
#print(pd.Series(data_result.iloc[1]))


# df_srs= pd.Series(data_result.iloc[1])
# df_to_list= []
# df_to_list.append(df_srs)
# print(df_to_list)

# 리스트 넣어줘야 insert가 가능?
#df_list= ",".join(df_to_list)
#print(df_list)
#class_list.append(df_list)
#print(class_list)

# barraID에 <index,ID>형태에서 ID만 남기게 전처리
#data_result = data_result.replace(r'[0-9]+\,','', regex=True)

#print(data_result)