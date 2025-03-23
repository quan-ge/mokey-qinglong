# 奇妙应用自动签到使用教程



## 获取token和id
请先安装“奇妙应用”APP，此软件为安卓端软件。


#### token
1. 安装 “HttpCanary” 。

2. 左上角三条杠 --＞ 打开设置中心

![奇妙应用_2](https://raw.githubusercontent.com/quan-ge/mokey-qinglong/refs/heads/main/help/jpg/qmyy_2.jpg "奇妙应用_2"）

3. httpcanary根证书 --＞ 导出根证书

![奇妙应用_3](https://raw.githubusercontent.com/quan-ge/mokey-qinglong/refs/heads/main/help/jpg/qmyy_3.jpg "奇妙应用_3")


4. 选择 .pem 格式保存。

5. 打开安卓系统设置，搜索或打开“加密和凭据”设置。

6. 选择“从储存设备中安装”或“安装CA证书”

7. 选择文件：“/Documents/HttpCanary/certs/HttpCanary.pem”

8. 打开“奇妙应用”，进入“我的”页面。

9. 回到“httpcanary”软件，点击右下角纸飞机图标开始抓包

10. 再次进入“奇妙应用”，刷新界面

11. 返回“httpcanary”，再次点击右下角纸飞机图标结束抓包。

12. 点击“奇妙应用”的那一段请求，按照如图所示，复制token

![奇妙应用_12](https://raw.githubusercontent.com/quan-ge/mokey-qinglong/refs/heads/main/help/jpg/qmyy_12.jpg "奇妙应用_12")

13. 记得找个地方保存token，并且不要发给别人或公开

#### 获取id
1. 在奇妙应用“我的”界面，点击头像

2. 来到个人主页，在点右上角三个点

3. 选“复制账户”

4. 这一串数字就是id

例如：“9551714”，这是我的账号id

## 配置脚本

1. 在青龙面板中添加两个环境变量：

> 名称:
> mokey_qmyy_token
>
> 值：
> 填你之前获取到的token
>

> 名称:
> mokey_qmyy_id
>
> 值：
> 填你之前获取到的id
>

2. 青龙面板主页找到“[mokey]奇妙应用自动签到”脚本

点击最后面三个点，选择启用

3. 最后点击运行，测试一下就大功告成了🎉🎉🎉
