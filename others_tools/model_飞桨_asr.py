# 安装
'''
pip install paddlespeech==1.2.0
pip install paddleaudio==1.0.1
'''
from paddlespeech.cli.asr.infer import ASRExecutor
audio = "zh.wav"
asr = ASRExecutor()
result = asr(audio_file=audio, model='conformer_online_wenetspeech')
print(result)