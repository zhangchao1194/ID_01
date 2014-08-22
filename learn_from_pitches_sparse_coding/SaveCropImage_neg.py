import Image
import glob
import os
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import SparseCoder
from time import time
from multiprocessing import Pool
import random 

if __name__ == '__main__':
    t0 = time()
    os.chdir("./neg_imgs")
    i = 0
    for image_file in glob.glob("*.png"):
        image_file = "/root/git/repos/ID_01/learn_from_pitches_sparse_coding/neg_imgs/" + image_file 
        im = Image.open(image_file)
        i=i+1
        for j in xrange(14):
            x = random.randint(0+16, im.size[0]-16)
            y = random.randint(0+16, im.size[1]-16)
            box = (x-16,y-16,x+16,y+16)
            crop_im = im.crop(box)
            crop_im.save("/root/git/repos/ID_01/learn_from_pitches_sparse_coding/imgs/articulations/neg/"+str(i)+".jpg")
    dt = time() - t0
    print 'done in %.2fs.' % dt
