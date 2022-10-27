import random

import cv2
import numpy as np
import requests
import json
import base64
import uuid
# width = 1024
# height = 576
from z01_gen_cartoon_pic import cfg
def get_img(img,url,step=20,promt_tail=""):
    h,w,c = img.shape
    if min(h, w) < 512:
        ratio = 512/min(h, w)
        h = int(h * ratio)
        w = int(w * ratio)
        img = cv2.resize(img, (w, h))

    height = h // 64 * 64
    width = w // 64 * 64


    np_img = cv2.resize(img,(width,height))
    retval, buffer = cv2.imencode('.png', np_img)
    pic_base64 = "data:image/png;base64,"+base64.b64encode(buffer).decode()
    jsn = json.load(open("a.txt"))
    jsn['data'][1] = cfg.promt + promt_tail
    jsn['data'][5] = pic_base64

    step = random.randint(cfg.step[0],cfg.step[1])  # step
    jsn['data'][10] = step

    CFG_scale = random.randint(cfg.CFG_scale[0],cfg.CFG_scale[1])  # CFG scale
    jsn['data'][18] = CFG_scale

    Denoising_strength = random.randint(cfg.Denoising_strength[0]*100,cfg.Denoising_strength[1]*100)/100  # Denoising strength
    jsn['data'][19] = Denoising_strength

    jsn['data'][26] = height  # height
    jsn['data'][27] = width  # width


    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=jsn, headers=headers)
    pic_base64 = json.loads(response.text)['data'][0][0]
    img_data = base64.b64decode(pic_base64.split("base64,")[-1])
    nparr = np.frombuffer(img_data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img_np,CFG_scale,Denoising_strength,step
