import shutil

import cv2
import numpy as np
import requests
import json
import base64
import uuid


jsn = json.load(open("a.txt"))
img = cv2.imread("1.png")
h,w,c = img.shape
radio = (w/h)/(1920/1080)
if radio<1:
    h_ = int(h*radio)
    len_up = (h-h_)//2
    img = img[len_up:h - len_up, :, :]
else:
    w_ = int(w*radio)
    len_left = (w-w_)//2
    img = img[:,len_left:w - len_left,  :]

width = 1024
height = 576
np_img = cv2.resize(img,(width,height))
# cv2.imwrite("res.png", np_img)
# 9/0
retval, buffer = cv2.imencode('.png', np_img)
pic_base64 = "data:image/png;base64,"+base64.b64encode(buffer).decode()
jsn['data'][5] = pic_base64  # height


# jsn['data'][10] = 2  # step
# jsn['data'][19] = 0.6  # denoising_strength
# jsn['data'][26] = 960  # height
# jsn['data'][27] = 1440  # width
# scale = 0.5
# width = int(1920* scale)
# height = 640#int(1080* scale)
# print(width,height)
# jsn['data'][27] = width # width
# jsn['data'][26] = height  # height

url = "http://127.0.0.1:7861/api/predict"
headers = {'content-type': 'application/json'}
response = requests.post(url, json=jsn, headers=headers)
pic_base64 = json.loads(response.text)['data'][0][0]
img_data = base64.b64decode(pic_base64.split("base64,")[-1])
nparr = np.frombuffer(img_data, np.uint8)
img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
name = str(uuid.uuid4())+".png"
cv2.imwrite(name, img_np)
shutil.move(name,"你好.png")
