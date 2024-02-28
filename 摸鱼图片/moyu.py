from flask import Flask,Response
import os
app = Flask(__name__)
# 获取今天的日期20240228
def get_today():
    import datetime
    today = str(datetime.date.today()).replace("-","")
    return today
# 截取一个图片的上边5%不显示
def cut_top(img):
    from PIL import Image
    img = Image.open(img)
    img_top = img.crop((0, img.height * 0.05, img.width,img.height ))
    img_top.save(os.path.join(img_dir,"today.png"))
    img_top.save(os.path.join(img_dir,"{}.png".format(get_today())))

# 下载图片
def download_img():
    url = "https://free.wqwlkj.cn/wqwlapi/moyu.php?type=image"
    import requests
    response = requests.get(url)
    with open(os.path.join(img_dir,"temp.png"), "wb") as f:
        f.write(response.content)
    cut_top(os.path.join(img_dir,"temp.png"))

@app.route('/')
def index():
    # 判断当天日期是否存在 不存在进行请求新的图片
    times = get_today()
    if not os.path.exists(os.path.join(img_dir,f"{times}.png")):
        print("更新了图片:",times)
        download_img()
    with open(os.path.join(img_dir,"today.png"), 'rb') as f:
            image = f.read()
    return Response(image, mimetype='image/jpeg')
img_dir = "./image"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)
app.run(host='0.0.0.0', port=8080)