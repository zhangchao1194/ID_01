import Image
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import SparseCoder
from time import time
from multiprocessing import Pool

if __name__ == '__main__':
    t0 = time()
    image_list = open("patchlist.txt")
    annotation = open("./imgs/annotation.txt")
    i = 0
    for image_file in image_list:
        image_file =  image_file.rstrip()
        im = Image.open(image_file)
        i=i+1
        line = annotation.readline()
        while line.split():
            str_class, str_x, str_y = line.split()
            #print image_file, str_class, str_x, str_y
            x = int(round(float(str_x)))
            y = int(round(float(str_y)))
            box = (x-16,y-16,x+16,y+16)
            crop_im = im.crop(box)
            crop_im.save("./imgs/articulations/"+str_class+"/"+str(i)+".jpg")
            #print box
            #print "./imgs/"+str_class+"/"+str(i)+".jpg"
            line = annotation.readline()

    dt = time() - t0
    print 'done in %.2fs.' % dt
