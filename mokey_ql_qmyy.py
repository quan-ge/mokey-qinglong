# cron:6 6 * * *
# const $ = new Env("[mokey]奇妙应用自动签到")
# V1.0.1
# 作者：全戈
# QUAN_GE

import requests
import datetime


# 用户ID和token
getEnvs_list = QLAPI.getEnvs({ "searchValue": "mokey_qmyy_token" })
YourToken = getEnvs_list['data']
YourToken = YourToken[ 0 ]
YourToken_name = YourToken['name']
if YourToken_name == 'mokey_qmyy_token':
    YourToken = YourToken[ 'value' ]
else:
    print('未在环境变量中添加token，出现错误，请翻阅官方文档')

getEnvs_list_2 = QLAPI.getEnvs({ "searchValue": "mokey_qmyy_id" })
YourUID = getEnvs_list_2['data']
YourUID = YourUID[ 0 ]
YourUID_name = YourUID['name']
if YourUID_name == 'mokey_qmyy_id':
    YourUID = YourUID[ 'value' ]
else:
    print('未在环境变量中添加ID，出现错误，请翻阅官方文档')

user_id = YourUID
token = YourToken

#获取时间
today = datetime.datetime.now()

# 签到和爆硬币API的端点
sign_url = "http://www.magicalapp.cn/user/api/signDays"
burst_url = f"https://www.magicalapp.cn/api/game/api/getCoinP?userId={user_id}"
headers = {
    'token': token,
    'Host': 'www.magicalapp.cn',
    'User-Agent': 'okhttp/4.9.3'
}

# 签到操作
sign_response = requests.get(sign_url, headers=headers)
if sign_response.status_code == 200:
    coin_count_sign = 5  # 签到成功，直接获取固定硬币数
    str_sign_response = str(sign_response)
    a_info = f"✅✅✅签到成功，响应：{sign_response.status_code}{str_sign_response}"
else:
    coin_count_sign = 0
    a_info = f"❌❌❌账号 {user_id} 签到失败，响应：{sign_response.status_code}"

# 爆硬币操作
burst_response = requests.get(burst_url, headers=headers)
if burst_response.status_code == 200:
    try:
        burst_data = burst_response.json()
        if isinstance(burst_data, dict) and burst_data.get("code") == "200":
            coin_count_burst = burst_data.get("data", 0)
            b_info = f"✅✅✅自动爆金币成功，获得 {coin_count_burst} 枚金币"
        else:
            b_info = f"❌❌❌账号 {user_id} 爆硬币失败，响应异常：{burst_data}"
            coin_count_burst = 0
    except ValueError:
        b_info = f"❌❌❌账号 {user_id} 爆硬币失败，响应不是有效JSON：{burst_response.text}"
        coin_count_burst = 0
else:
    b_info = f"❌❌❌账号 {user_id} 爆硬币失败，响应状态码异常：{burst_response.status_code}"
    coin_count_burst = 0

# 总硬币数
total_coins = coin_count_sign + coin_count_burst
str_total_coins = str( total_coins )

info = f"""
账号 {user_id} 签到完成✅✅✅
猴子脚本-奇妙应用自动签到
~~~~~~~~~~
签到信息：
{a_info}
{b_info}
一共获得 {total_coins} 枚金币。
~~~~~~~~~~
运行时间：{today}
数据仅供参考，重复签到可能导致数据不准~
~~~~~~~~~~
脚本来自mokey项目，作者全戈
项目地址：
https://github.com/quan-ge/mokey-qinglong/
"""

print(info)

# 调用青龙api发送通知
print("发送通知...")
print(QLAPI.systemNotify({ "title": "自动签到通知-奇妙应用", "content": info }))
