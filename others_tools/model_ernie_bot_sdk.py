'''
Author: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
Date: 2024-02-28 16:14:51
LastEditors: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
LastEditTime: 2024-02-28 16:15:06
FilePath: \docker_service\api_tools\others_tools\model_en.py
Description: 爱喝水的木子
Copyright (c) now_year by 爱喝水的木子 email: 50564847+ice-a@users.noreply.github.com, All Rights Reserved.
'''
# ERNIE Bot SDK
import erniebot

erniebot.api_type = 'aistudio'
erniebot.access_token = '<access-token-for-aistudio>'

response = erniebot.ChatCompletion.create(
    model='ernie-turbo',
    messages=[{
        'role': 'user',
        'content': "请问你是谁？"
    }, {
        'role': 'assistant',
        'content':
        "我是百度公司开发的人工智能语言模型，我的中文名是文心一言，英文名是ERNIE-Bot，可以协助您完成范围广泛的任务并提供有关各种主题的信息，比如回答问题，提供定义和解释及建议。如果您有任何问题，请随时向我提问。"
    }, {
        'role': 'user',
        'content': "我在深圳，周末可以去哪里玩？"
    }])

print(response.get_result())