'''
Author: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
Date: 2024-02-27 09:16:39
LastEditors: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
LastEditTime: 2024-02-27 09:20:25
FilePath: \docker_service\api_xingqisi\1.py
Description: 爱喝水的木子
Copyright (c) now_year by 爱喝水的木子 email: 50564847+ice-a@users.noreply.github.com, All Rights Reserved.
'''
from flask import Flask,jsonify
import random
app = Flask(__name__)

with open("kfcyl.txt","r",encoding="utf-8")as f:
    data = f.readlines()

@app.route('/')
def index():
    random_number = random.randint(0,len(data))
    return jsonify({"code":"200","msg":data[random_number]})

app.run(host='0.0.0.0', port=8080)