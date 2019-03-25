# 北邮ngw自动登录脚本1.0版本
### 使用说明

1. 将ngw.bupt.edu.cn的账户密码写在user.config 文件中

* 例如：
user.config

===============(start of user.config)===========
> 2016211888

> wozuishuai123

===============(end of user.config)============

2. 将“Login.exe"文件创建快捷方式，并将快捷方式复制到

> %USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

目录下，即可开机启动，自动连接校园网，避免每次输入网址，账号密码。
