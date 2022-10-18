import shutil

import cv2
import numpy as np
import requests
import json
import base64
import uuid
width = 1024
height = 576

def get_img(img,url,step=20):
    h,w,c = img.shape
    # radio = height/h
    # w_new = int(w*radio)
    # img = cv2.resize(img, (w_new, height))
    #
    # if w_new<width:
    #     np_img = np.zeros((height, width, 3))
    #     len_left = (width-w_new)//2
    #     np_img[:, len_left:len_left + w_new, :] = img
    # else:
    #     len_left = (w_new - width) // 2
    #     np_img = img[:,len_left:len_left+width,  :]
    radio = (w/h)/(1920/1080)
    if radio<1:
        h_ = int(h*radio)
        len_up = (h-h_)//2
        img = img[len_up:h - len_up, :, :]
    else:
        w_ = int(w*radio)
        len_left = (w-w_)//2
        img = img[:,len_left:w - len_left,  :]


    np_img = cv2.resize(img,(width,height))
    # cv2.imwrite("res.png", np_img)
    # 9/0
    retval, buffer = cv2.imencode('.png', np_img)
    pic_base64 = "data:image/png;base64,"+base64.b64encode(buffer).decode()
    jsn = json.load(open("a.txt"))
    jsn['data'][5] = pic_base64
    jsn['data'][10] = step  # step

    jsn['data'][26] = height  # height
    jsn['data'][27] = width  # width


    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=jsn, headers=headers)
    pic_base64 = json.loads(response.text)['data'][0][0]
    img_data = base64.b64decode(pic_base64.split("base64,")[-1])
    nparr = np.frombuffer(img_data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img_np
    # name = str(uuid.uuid4())+".png"
    # cv2.imwrite(name, img_np)
    # shutil.move(name,"你好.png")
