import os

# 경로 설정
dir_path = "D:\\Barra\\daily\\"

file_list=[]

for (root, directories, files) in os.walk(dir_path):
    for d in directories:
        d_path = os.path.join(root, d)
        print(d_path)

    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        file_list.append(file_path)

print(file_list)


