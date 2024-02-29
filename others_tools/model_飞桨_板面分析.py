'''
Author: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
Date: 2024-02-29 09:26:30
LastEditors: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
LastEditTime: 2024-02-29 09:29:38
FilePath: \docker_service\api_tools\others_tools\model_飞桨_板面分析.py
Description: 爱喝水的木子
Copyright (c) now_year by 爱喝水的木子 email: 50564847+ice-a@users.noreply.github.com, All Rights Reserved.
'''
# 安装
'''
pip install "paddleocr>=2.6.1.0" --user
'''

# 图像方向分类_板面分析_表格识别
'''
! pip install paddleclas
! paddleocr --image_dir=1.png --type=structure --image_orientation=true
'''
# 版面分析+表格识别
'''
! paddleocr --image_dir=1.png --type=structure
'''
# 版面分析
'''
! paddleocr --image_dir=1.png --type=structure --table=false --ocr=false
'''
# 表格识别
'''
! paddleocr --image_dir=table.jpg --type=structure --layout=false
'''