from PIL import Image
import os
import glob


def convert_and_delete_jpg(folder_path):
    image_extensions = ["*.jpg", "*.jpeg"]

    for ext in image_extensions:
        for img_path in glob.glob(os.path.join(folder_path, "**", ext), recursive=True):
            # 打开图片
            img = Image.open(img_path)
            # 转换为png格式
            png_path = os.path.splitext(img_path)[0] + ".png"
            print("转换中:", img_path)
            img.save(png_path, "PNG")
            # 删除原jpg图片
            os.remove(img_path)
            print("删除中:", img_path)


folder_path = r"C:\Users\DM\Desktop\1"
convert_and_delete_jpg(folder_path)
