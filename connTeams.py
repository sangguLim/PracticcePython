import pymsteams
def webhook(channelName='normal'): # default 일반채널로 설정
    if channelName=='normal':
        WebHook= 'normal hook_url'
    if channelName=='BarraReport':
        WebHook='BarraReport hook_url'
    if channelName=='BarraError':
        WebHook='BarraError hook_url'
    if channelName=='FactorReport':
        WebHook='FactorReport hook_url'
    #myTeamsMessage = pymsteams.connectorcard(WebHook)

    return WebHook