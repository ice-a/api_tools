# 使用方法
## docker
### 构建
```bash
docker build -t moyutime .
```
### 创建容器
```bash
docker run -itd --name momoyu -p 8081:8080 moyutime
```
## python直接运行
### 需要的包
```
flask
requests
pillow
```
### 执行
```
python moyu.py
```
