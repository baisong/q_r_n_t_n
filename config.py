# Import the optimizers we need
#from .optimizeimages import pngnq, optipng

worlds["world"] = "/home/oren/.minecraft/saves/q r n t n (World 1)-3"

renders["daytime"] = {
    "world":"world",
    "title":"day",
    "rendermode":smooth_lighting,
    "imgformat":"webp",
    "imgquality":75,
    "imglossless":False,
    #"optimizeimg":[pngnq(sampling=1), optipng(olevel=3)],
}

outputdir = "/home/oren/github/baisong/q_r_n_t_n"
