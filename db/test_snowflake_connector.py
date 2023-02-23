import pandas as pd
from glue.snowflake import Snowflake
from snowflake.connector import cursor
from glue.snowflake import Snowflake
import snowflake

# pandas df로 읽으려면 아래와 같은 함수 사용
#fetch_pandas_all()
#fetch_pandas_batches()


# snowflake 커넥션
# Snowflake 함수는 glue 파일 내 함수
sf = Snowflake(
        role='alpha_platform',
        warehouse='COMPUTE_WH',
        database='alpha_platform',
        user='sanggu.lim',
        password='Dlatkdrn95!')

with sf.connect() as conn:
    try:
        sclt= conn.cursor().execute('select top 10 * from alpha_platform.temp.date')
        print(sclt) 
    finally:
        conn.close()