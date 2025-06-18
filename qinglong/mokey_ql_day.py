# cron:6 0 * * *
# const $ = new Env("[mokey]每日通知")
# 作者：QUAN_GE
# 

import requests
import random
from time import time
from time import sleep
from datetime import datetime
import json

def day():
    # 延时运行脚本，以防万一
    time = random.uniform(0, 20)
    stltime = str(time)
    print("延迟运行(s):" + stltime)
    sleep(time)

    # 万年历
    print("万年历>>>>>>")
    current_dateTime = datetime.now()
    y = current_dateTime.year
    m = current_dateTime.month
    d = current_dateTime.day
    d = d + 1
    t = "%s-%s-%s" % (y, m, d) 

    data = {
        'sun': t
    }
    print(data)
    response = requests.get('https://www.36jxs.com/api/Commonweal/almanac', params=data)
    gett = json.loads(response.text)
    print(gett)
    gettt = gett['data']
    print(gettt)

    # 音乐
    #     获取音乐
    response_3 = requests.get('https://free.wqwlkj.cn/wqwlapi/wyy_random.php?type=json')
    print(response_3)
    getmusic = json.loads(response_3.text)
    print(getmusic)
    getmusic = getmusic['data']
    print(getmusic)
    #     短链接
    data = {
        'url': getmusic['url']
    }
    response_4 = requests.get('https://url.hdgxl.com/api.php', params=data)
    print(response_4)
    get333 = json.loads(response_4.text)
    print(get333)
    getmusicurl = get333['code']
    print(getmusicurl)
    #     生成通知
    info_music = f"""为您推荐：{getmusic['artistsname']} 的 {getmusic['name']}
    歌曲下载链接：{getmusicurl}"""
    print(info_music)

    # 版本检测
    print("版本检测>>>>>>")
    response_2 = requests.get('https://mokeyqlapi.120322.xyz/now.json')
    print(response_2)
    now = json.loads(response_2.text)
    now = now["now"]
    print(now)
    if now == "1.2.4":
        info2 = "当前已经为最新版！"
    else:
        info2 = f"最新版为“{now}”，运行订阅以更新！！"

    # 通知
    info = f"""
    猴子脚本-（DAY）更新检查
    ~~~~~~~~~~
    明天的黄历：
    公历日期：{gettt['GregorianDateTime']}
    农历日期：{gettt['LunarDateTime']}
    公历节日：{gettt['GJie']}
    农历节日：{gettt['LJie']}
    今日宜：{gettt['Yi']}
    今日忌：{gettt['Ji']}
    节气：{gettt['SolarTermName']}
    ~~~~~~~~~~
    {info_music}
    ~~~~~~~~~~
    版本更新检查：
    {info2}
    ~~~~~~~~~~
    脚本来自mokey项目，作者全戈
    项目地址：
    https://github.com/quan-ge/mokey-qinglong/
    """
    print(info)
    # 调用青龙api发送通知
    print("发送通知...")
    print(QLAPI.systemNotify({ "title": "自动签到通知-DAY", "content": info }))



try:
    day()
except Exception as e:
    print("脚本运行出错！!!!")
    error_info = f"""
    猴子脚本-（DAY）更新检查
    ~~~~~~~~~~
    脚本运行出错，请检查日志！
    错误信息：{str(e)}
    出错行：{str(e.__traceback__.tb_lineno)}
    ~~~~~~~~~~
    反馈渠道：
    https://github.com/quan-ge/mokey-qinglong/issues
    quan@email.120322.xyz
    ~~~~~~~~~~
    脚本来自mokey项目，作者全戈
    项目地址：
    https://github.com/quan-ge/mokey-qinglong/
    """
    print(error_info)
    print(QLAPI.systemNotify({ "title": "自动签到通知-DAY", "content": error_info }))

