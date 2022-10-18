import cv2
import shutil
from PIL import Image
import os
import uuid

from tqdm import tqdm

import client_util

url = "http://127.0.0.1:7860/api/predict"
dir_out_img = "z_out_img/"
dir_in_img = "z_img/"

if not os.path.exists(dir_out_img):
    os.makedirs(dir_out_img)

lst_dir = [dir_in_img+i+"/" for i in os.listdir(dir_in_img)]
lst_dir.sort(reverse=True)

# 每个文件夹遍历X次
for i in range(10*len(lst_dir)):
    print(i)
    dir_cur = lst_dir[i%len(lst_dir)]
    lst_pic = [dir_cur+i for i in os.listdir(dir_cur)]
    for pic in tqdm(lst_pic):
        url_img = dir_out_img + f"{uuid.uuid4()}.png"
        if pic.lower().endswith(".png"):
            shutil.copy(pic, url_img)
        elif pic.lower().endswith(".webp"):
            img = Image.open(pic)
            img.save(url_img)
        else:
            continue

        img = cv2.imread(url_img)
        h,w,c = img.shape
        if h<100 or w<100:
            continue
        img_np = client_util.get_img(img,url,step=30)

        cv2.imwrite(url_img, img_np)
        shutil.move(url_img, dir_out_img + dir_cur.split("/")[1] + url_img[-17:])

