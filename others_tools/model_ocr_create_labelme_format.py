#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
import os
from PIL import Image
from paddleocr import PaddleOCR


# 百度飞桨的识别结果生成json
def ocr_result_create_json(result, imageHeight, imageWidth, imagePath, save_file_name):
    template_data = {
        "version": "3.16.7",
        "flags": {},
        "shapes": [],
        "lineColor": [0, 255, 0, 128],
        "fillColor": [255, 0, 0, 128],
        "imagePath": imagePath,
        "imageHeight": imageHeight,
        "imageWidth": imageWidth,
        "imageData": None,
    }
    shapes = []
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
            _label_result = line[1]
            _point = line[0]
            temp = {
                "label": _label_result[0],
                "line_color": None,
                "fill_color": None,
                "points": _point,
                "shape_type": "polygon",
                "flags": {},
            }
            shapes.append(temp)
    template_data["shapes"] = shapes
    with open(save_file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(template_data, ensure_ascii=False, indent=4))


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
ocr = PaddleOCR(
    use_angle_cls=False, lang="ch", ocr_version="PP-OCRv4"
)
image_path = r"C:\Users\DM\Desktop\试标\image"
save_json = r"C:\Users\DM\Desktop\试标\json"
for img in os.listdir(image_path):
    t = os.path.join(image_path, img)
    json_file = os.path.join(save_json, img.replace(".png", ".json"))
    img_size = Image.open(t)
    x, y = img_size.size
    ocr_result_create_json(ocr.ocr(t, cls=True), y, x, img, json_file)
