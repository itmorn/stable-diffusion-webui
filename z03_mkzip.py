import shutil

import os
from tqdm import tqdm

dir_out_zip = "z_out_zip/"
shutil.rmtree(dir_out_zip,ignore_errors=True)
if not os.path.exists(dir_out_zip):
    os.makedirs(dir_out_zip)


for idx,name_pic in tqdm(enumerate(os.listdir("z_out_img"))):
    # if idx%3==0:
    #     continue
    geci = name_pic[:-17]+"/"
    if not os.path.exists(dir_out_zip+geci):
        os.makedirs(dir_out_zip+geci)
    shutil.copy(f"z_out_img/{name_pic}",dir_out_zip+geci+name_pic)


os.system("rm -f test.zip")
os.system("zip -r test.zip z_out_zip")

