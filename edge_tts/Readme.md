# 使用方法
## docker
### 构建
```bash
docker build -t tts_api .
```
### 创建容器
```bash
docker run -itd --name tts_api -p 5000:5000 moyutime
```
## python直接运行
### 需要的包
```
edge-tts
torchaudio
flask
```
### 执行
```
python app.py
```
