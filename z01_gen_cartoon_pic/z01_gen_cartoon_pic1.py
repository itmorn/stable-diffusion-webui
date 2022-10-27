import sys

import cv2
import shutil
import os
import uuid
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '../', '../')))
from z01_gen_cartoon_pic import util

url = f"http://127.0.0.1:786{__file__[-4]}/api/predict"
dir_in_img = "in_img/"
dir_out_img = "out_img/"

# shutil.rmtree(dir_out_img, ignore_errors=True)
# if not os.path.exists(dir_out_img):
#     os.makedirs(dir_out_img)

lst_pic = [dir_in_img + i for i in os.listdir(dir_in_img)]

count = 0
for i in range(2000):
    for pic in lst_pic:

        img = cv2.imread(pic)
        h, w, c = img.shape
        if h < 100 or w < 100:
            continue
        promt_tail = os.path.basename(pic).split("#")[0]
        img_np,CFG_scale,Denoising_strength,step = util.get_img(img, url,step=20,promt_tail=promt_tail)
        # url_img = dir_out_img + f"{uuid.uuid4()}"[-12:] + f"{uuid.uuid4()}.png"
        url_img = f"{dir_out_img}CFG_{str(CFG_scale)[:3]}_Denoising_{str(Denoising_strength)[:4]}_step_{step}_{str(uuid.uuid4())[-12:]}.png"
        cv2.imwrite(url_img, img_np)
        count +=1
        print(count)

