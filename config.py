# Import the optimizers we need
#from .optimizeimages import pngnq, optipng

worlds["world"] = "/home/oren/.minecraft/saves/q r n t n 2021-02-15 snapshot"

texturepath = "/home/oren/.minecraft/versions/21w06a/21w06a.jar"

renders["daytime"] = {
    "world":"world",
    "title":"day",
    #"rendermode":smooth_lighting,
    "imgformat":"webp",
    "imgquality":25,
    "imglossless":False,
    #"optimizeimg":[pngnq(sampling=1), optipng(olevel=3)],
}

outputdir = "/home/oren/github/baisong/q_r_n_t_n"
