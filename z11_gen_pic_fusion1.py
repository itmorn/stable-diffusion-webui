import base64
import json

import cv2
import numpy as np
import requests
import shutil
import os
import uuid

from tqdm import tqdm


url = f"http://127.0.0.1:786{__file__[-4]}/api/predict"
dir_out_img = "z11_out_img_fusion/"

# shutil.rmtree(dir_out_img,ignore_errors=True)
# if not os.path.exists(dir_out_img):
#     os.makedirs(dir_out_img)

jsn = json.load(open("z_pic_fusion.txt"))
import z11_cfg
jsn['data'][0] = z11_cfg.promt
jsn['data'][17] = z11_cfg.height
jsn['data'][18] = z11_cfg.width

# 每个文件夹遍历X次
for i in tqdm(range(1000)):
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=jsn, headers=headers)
    pic_base64 = json.loads(response.text)['data'][0][0]
    img_data = base64.b64decode(pic_base64.split("base64,")[-1])
    nparr = np.frombuffer(img_data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    url_img = dir_out_img + f"{uuid.uuid4()}.png"
    cv2.imwrite(url_img, img_np)
    shutil.move(url_img, dir_out_img+ url_img[-17:])

