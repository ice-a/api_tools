'''
Author: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
Date: 2024-02-29 09:12:36
LastEditors: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
LastEditTime: 2024-02-29 09:19:08
FilePath: \docker_service\api_tools\others_tools\model_飞桨_信息抽取.py
Description: 爱喝水的木子
Copyright (c) now_year by 爱喝水的木子 email: 50564847+ice-a@users.noreply.github.com, All Rights Reserved.
'''
# 安装
'''
pip install --upgrade paddlenlp
pip show paddlenlp
'''
from pprint import pprint
from paddlenlp import Taskflow

# 实体抽取
def uie_base():
    schema = ['时间', '选手', '赛事名称'] # Define the schema for entity extraction
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    # ie_en = Taskflow('information_extraction', schema=schema, model='uie-base-en')
    # Better print results using pprint
    pprint(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")) 

# 关系抽取
def uie_base_2():
    schema = {'竞赛名称': ['主办方', '承办方', '已举办次数']} # Define the schema for relation extraction
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    ie.set_schema(schema) # Reset schema
    pprint(ie('2022语言与智能技术竞赛由中国中文信息学会和中国计算机学会联合主办，百度公司、中国中文信息学会评测工作委员会和中国计算机学会自然语言处理专委会承办，已连续举办4届，成为全球最热门的中文NLP赛事之一。'))

# 事件抽取
def uie_base_3():
    schema = {'地震触发词': ['地震强度', '时间', '震中位置', '震源深度']} # Define the schema for event extraction
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    ie.set_schema(schema) # Reset schema
    pprint(ie('中国地震台网正式测定：5月16日06时08分在云南临沧市凤庆县(北纬24.34度，东经99.98度)发生3.5级地震，震源深度10千米。'))

# 评论观点抽取
def uie_base_4():
    schema = {'评价维度': ['观点词', '情感倾向[正向，负向]']} # Define the schema for opinion extraction
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    ie.set_schema(schema) # Reset schema
    pprint(ie("店面干净，很清静，服务员服务热情，性价比很高，发现收银台有排队")) # Better print results using pprint

# 情感分析
def uie_base_5():
    schema = '情感倾向[正向，负向]' # Define the schema for sentence-level sentiment classification
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    ie.set_schema(schema) # Reset schema
    ie('这个产品用起来真的很流畅，我非常喜欢')

# 跨任务抽取
def uie_base_6():
    schema = ['法院', {'原告': '委托代理人'}, {'被告': '委托代理人'}]
    ie = Taskflow('information_extraction', schema=schema, model='uie-base')
    ie.set_schema(schema)
    pprint(ie("北京市海淀区人民法院\n民事判决书\n(199x)建初字第xxx号\n原告：张三。\n委托代理人李四，北京市 A律师事务所律师。\n被告：B公司，法定代表人王五，开发公司总经理。\n委托代理人赵六，北京市 C律师事务所律师。")) # Better print results using pprint