# [mokey]奇妙应用自动签到
# 作者：QUAN_GE

# 请修改成你的token和id
# 参考：https://github.com/quan-ge/mokey-qinglong/blob/main/help/qmyy.md#%E8%8E%B7%E5%8F%96token%E5%92%8Cid
# 
# 例如：
# user_id = "12345555"
# token = "sgi34ygvdvyyv89wqhyv98ch392yg9v7y"
user_id = "[YourUID]"
token = "[YourToken]"




# 下面的就不要动了，除非你知道自己在做什么
# 这个脚本不会更新了，有问题不要反馈，反馈了我也不想修
import requests
import datetime
import json
current_dateTime = datetime.now()
y = current_dateTime.year
m = current_dateTime.month
d = current_dateTime.day
t = "%s-%s-%s" % (y, m, d) 
today = datetime.datetime.now()
sign_url = "http://www.magicalapp.cn/user/api/signDays"
burst_url = f"https://www.magicalapp.cn/api/game/api/getCoinP?userId={user_id}"
headers = {
    'token': token,
    'Host': 'www.magicalapp.cn',
    'User-Agent': 'okhttp/4.9.3'
}
sign_response = requests.get(sign_url, headers=headers)
if sign_response.status_code == 200:
    coin_count_sign = 5  # 签到成功，直接获取固定硬币数
    str_sign_response = str(sign_response)
    a_info = f"✅✅✅签到成功，响应：{sign_response.status_code}{str_sign_response}"
else:
    coin_count_sign = 0
    a_info = f"❌❌❌账号 {user_id} 签到失败，响应：{sign_response.status_code}"
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
total_coins = coin_count_sign + coin_count_burst
str_total_coins = str( total_coins )
info = f"""
猴子脚本-奇妙应用自动签到
账号 {user_id} 签到完成✅✅✅
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
file = f'./logs/qmyy/{t}.log'
print(f"日志文件：{file}")
fo = open(file, mode='x')
fo.write( info )
fo.close()

