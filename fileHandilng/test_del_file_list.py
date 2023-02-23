###############################################################
# Date: 2022-01-03
# Writer: sangguLim
# content: Delete files containing specific statements
# status: active
###############################################################

import os


def file_remove(Path: str,txt_pattern: str):
    #dir_path = "D:\\Barra\\history_csv\\"   

    for (root, directories, files) in os.walk(Path):
        for file in files:
            if txt_pattern in file:
                file_path = os.path.join(root, file)
                #print(file_path)
                if os.path.isfile(file_path):
                    os.remove(file_path)


if __name__=='__main__':
    dir_path = "D:\\Barra\\history_csv\\"   
    pattern= '_2015'
    file_remove(dir_path,pattern)