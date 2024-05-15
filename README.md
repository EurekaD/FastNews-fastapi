# 毕业设计： 基于Transformer的中文新闻摘要web应用 fastapi的后端

## app
- setting 配置信息
- database 数据库连接

# auth
- captcha 验证码
- models 数据库交互
- router 路由
- schemas 模式，交互的数据格式
- services 服务函数，

# model
- pegasus PEGASUS模型目录
- router
- schemas
- services
- test 模型测试文件

# res
静态文件，词云字体文件

# utils
- decorators 装饰器
- image_encoder 把image转化为字符流
- login_code_gen 验证码图片生成，随机生成图片
- password 处理密码的函数，将密码hash，验证用户输入的密码
- token 创建token

# wordcloud
词云的相关内容
router
schemas
services 

# main.py
运行此文件即可开启后端服务，

# fastnews.env
配置文件，数据库的连接信息，jwt的密钥等