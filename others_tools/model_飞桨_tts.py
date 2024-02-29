'''
Author: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
Date: 2024-02-29 09:19:45
LastEditors: 爱喝水的木子 50564847+ice-a@users.noreply.github.com
LastEditTime: 2024-02-29 09:20:43
FilePath: \docker_service\api_tools\others_tools\model_飞桨_tts.py
Description: 爱喝水的木子
Copyright (c) now_year by 爱喝水的木子 email: 50564847+ice-a@users.noreply.github.com, All Rights Reserved.
'''
# 安装
'''
pip install paddlespeech
'''
from paddlespeech.cli.tts import TTSExecutor
tts_executor = TTSExecutor()
wav_file = tts_executor(
    text="热烈欢迎您在 Discussions 中提交问题，并在 Issues 中指出发现的 bug。此外，我们非常希望您参与到 Paddle Speech 的开发中！",
    output='output.wav',
    am='fastspeech2_mix',
    voc='hifigan_csmsc',
    lang='mix',
    spk_id=174)