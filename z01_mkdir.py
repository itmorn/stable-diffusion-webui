import os

os.makedirs("z_img")
lst_str_geci = """
窗透初晓
日照西桥
云自摇
想你当年荷风微摆的衣角
木雕流金
岁月涟漪
七年前封笔
因为我今生挥毫只为你
雨打湿了眼眶
年年倚井盼归堂
最怕不觉泪已拆两行
我在人间彷徨
寻不到你的天堂
东瓶西镜放
恨不能遗忘
又是清明雨上
折菊寄到你身旁
把你最爱的歌来轻轻唱
""".split("\n")

lst_str_geci = [i for i in lst_str_geci if i.strip()!=""]

print(lst_str_geci)
for i,str_geci in enumerate(lst_str_geci):
    os.makedirs(f'z_img/{"%02d" % i+"_" + str_geci}')
