import os

os.makedirs("z_img")
lst_str_geci = """
你在南方的艳阳里，大雪纷飞
我在北方的寒夜里，四季如春
如果天黑之前来得及，我要忘了你的眼睛
穷极一生，做不完一场梦
他不再和谁谈论相逢的孤岛
因为心里早已荒无人烟
他的心里再装不下一个家
做一个只对自己说谎的哑巴
他说你任何为人称道的美丽
不及他第一次遇见你
时光苟延残喘无可奈何
如果所有土地连在一起
走上一生只为拥抱你
喝醉了他的梦，晚安
""".split("\n")

lst_str_geci = [i for i in lst_str_geci if i.strip()!=""]

print(lst_str_geci)
for i,str_geci in enumerate(lst_str_geci):
    os.makedirs(f'z_img/{"%02d" % i+"_" + str_geci}')
