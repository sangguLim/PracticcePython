import sys
sys.path.append("C:\\Users\\USER\\Documents\\config\\")

import connTeams


WebHook= connTeams.webhook()
TeamsMsg = connTeams.pymsteams.connectorcard(WebHook)      
send_comment="> **팩터연산 끝났으니, 확인 부탁 드립니다!!!!!!**"
TeamsMsg.text(send_comment)
TeamsMsg.send()