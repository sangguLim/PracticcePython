# -- coding: utf-8 --
# ------------------------------------------------------------------------------ #
# 파일명   :   test_send_email
# 작성자   :   sanggu.lim
# 작성일   :   2023년 2월 08일
# 작성목적 :   Test Message Send to Mailing
# ------------------------------------------------------------------------------ #
#-*- coding: utf-8 -*-

import smtplib

from email.mime.text import MIMEText

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

gmail_username = "data.ai.lim39@gmail.com"
sendUser = "data.ai.lim39@gmail.com"
ReceiveUser = "data.ai.lim39@gmail.com"
gmail_pwd = "lpjgjvrnlqnpcnxl"

# 로그인 인증
s.login(gmail_username, gmail_pwd)

# 보낼 메시지 설정
msg = MIMEText('내용 : 본문내용 테스트입니다.')
msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

# 메일 보내기 
# s.sendmail("보내는 이메일", "받는 이메일", msg.as_string())
s.sendmail(sendUser, ReceiveUser, msg.as_string())

# 세션 종료
s.quit()