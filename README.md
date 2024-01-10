# 如何使用？ 
1、Fork项目到自己的仓库

2、点击Settings -> 点击选项卡 Secrets and variables -> 点击Actions -> New repository secret

(1)目前预设3个，再多个的话，需要对应调整下代码，也很简单

因为考虑cookie中的特殊字符，暂时不考虑用字符拼接多个，再去py里切割的方案

(2)关于Bark推送，不用的话填空即可


    | Name   | Secret                           |
    | ------ | ------------------------------- |
    | COOKIE1  | 第一个Cookie |
    | COOKIE2  | 第二个Cookie |
    | COOKIE3  | 第三个Cookie |
    | BARK_DEVICEKEY  | IOS应用Bark 推送密钥 |
    | BARK_ICON  | IOS应用Bark 推送的图标 |

3、点击Actions -> 选择hifini-sign -> 点击Run workflow 运行即可



感谢 https://github.com/Xramas/HiFiNi-Auto-Sign 提供思路
