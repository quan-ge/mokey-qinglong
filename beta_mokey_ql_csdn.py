# cron:6 0 * * *
# const $ = new Env("[mokey]CSDN自动签到")
# Vbeta1.0
# 作者：全戈
# QUAN_GE


import requests
headers = {
'accept':'application/json, text/plain, */*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
'cache-control':'no-cache',
'content-length':'241',
'content-type':'application/json;charset=UTF-8',
'cookie':'uuid_tt_dd=10_20644902740-1585309016706-911567; dc_sessioB%252522request%25255Fid%252522%25253A%252522160601203519724842915651%2525232bec4a3997715ac=1606012070; log_Id_click=514; dc_tos=qk6euh; log_Id_pv=1710',
'origin':'https://i.csdn.net',
'pragma':'no-cache',
'referer':'https://i.csdn.net/',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
data = {
'ip':'',
'platform':'pc-my',
'product':'pc',
'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
'username':'a12355556',
'uuid':'10_20644902740-1585309016706-911567'
}
r = requests.post("https://me.csdn.net/api/LuckyDraw_v2/signIn",headers=headers,data=data).content.decode("unicode_escape")
info 
print(r)                 
