import paramiko

# 변수를 선언해주고 초기 설정을 합니다.
host = "sftp.barra.com" # 실제 접속할 주소를 입력하세요
port = 22 # 그냥 22넣어주면 됩니다.
transprot = paramiko.transport.Transport(host,port)
userId = "ybozvdxq"  # user_id
password = 'DYzP0qjD>kZ9B5Kn8z<8' # password

# 연결
transprot.connect(username = userId, password = password)
sftp = paramiko.SFTPClient.from_transport(transprot)

remotepath = '/us/usmed/SMD_USMEDS_100_ETF_221031.zip' # sftp에 업로드 될때 파일 경로와 파일이름(이렇게 저장이 됨)을 써줍니다.
#remotepath = '/history/usmed/sm/daily/SMD_USMED_100_D_1995.zip' # sftp에 업로드 될때 파일 경로와 파일이름(이렇게 저장이 됨)을 써줍니다.
localpath  = 'D:\\Barra\\SMD_USMEDS_100_ETF_221031.zip' # local피시의 파일 경로와 파일이름(pc에 저장되어있는 파일이름)을 써줍니다.
# Upload - 파일 업로드
#sftp.put(localpath, remotepath)

# Get - 파일 다운로드
sftp.get(remotepath, localpath) # 위에 put과 반대로 생각하면 됩니다. remotepath에 sftp경로와 filename을 맞춰주시고, localpath에 다운로드 원하는 파일경로와 filename...

# Close - 꼭 닫아줍시다.
sftp.close()
transprot.close()