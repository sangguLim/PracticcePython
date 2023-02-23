import zipfile
from pathlib import Path
import pandas as pd



def replace_point(file_nm):
    result = file_nm.replace(".","_")
    return result

def zip_uncompress(file_nm):
    PATH = 'D:\\Barra\\Sample\\'
    SAVE_PATH = 'D:\\Barra\\uncompress\\'
    # 압축 해제 하기
    with zipfile.ZipFile(PATH+ file_nm + '.zip', 'r') as existing_zip:
        existing_zip.extractall(SAVE_PATH)