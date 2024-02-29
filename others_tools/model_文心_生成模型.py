# 安装
'''
!pip install --upgrade wenxin-api
'''
# -*- coding: utf-8 -*
import wenxin_api # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.text_to_image import TextToImage
wenxin_api.ak = "your_ak"
wenxin_api.sk = "your_sk"
input_dict = {
    "text": "睡莲",
    "style": "油画"
}
rst = TextToImage.create(**input_dict)
print(rst)