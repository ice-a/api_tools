import os.path

from flask import Flask, request, make_response, render_template
from werkzeug.datastructures import FileStorage
from datetime import datetime
import edge_tts  # tts音频

app = Flask(__name__)

config = {
    "male": ["zh-CN-YunjianNeural", "zh-CN-YunxiNeural", "zh-CN-YunxiaNeural", "zh-CN-YunyangNeural",
             "zh-HK-WanLungNeural", "zh-TW-YunJheNeural", "zu-ZA-ThembaNeural"],
    "female": ["zh-CN-XiaoxiaoNeural", "zh-CN-XiaoyiNeural", "zh-CN-liaoning-XiaobeiNeural",
               "zh-CN-shaanxi-XiaoniNeural", "zh-HK-HiuGaaiNeural", "zh-HK-HiuMaanNeural", "zh-TW-HsiaoChenNeural",
               "zh-TW-HsiaoYuNeural", "zu-ZA-ThandoNeural"]
}


# 生成tts音频
def create_tts_audio(text, speaker_voice):
    # 获取时间戳
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    OUTPUT_FILE = f"./audio/{timestamp}.wav"

    communicate = edge_tts.Communicate(text,
                                       speaker_voice,
                                       rate='+0%',
                                       volume='+0%',
                                       pitch='+50Hz')
    communicate.save_sync(OUTPUT_FILE)
    return OUTPUT_FILE


# 定义一个默认页面
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/generate_wav', methods=['POST'])
def generate_wav():
    # 解析 JSON 数据
    data = request.get_json()
    text_data = data['text']
    speaker_voice = data['speaker_voice']
    audio_file_name = create_tts_audio(text_data, speaker_voice)
    # 读取生成的.wav文件
    wav_file = FileStorage(filename=audio_file_name)
    wav_file.stream = open(audio_file_name, 'rb')

    # 创建响应
    response = make_response(wav_file.stream)
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(audio_file_name))

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
