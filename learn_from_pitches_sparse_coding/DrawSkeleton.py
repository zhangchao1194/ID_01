import Image
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import SparseCoder
from time import time
from multiprocessing import Pool
import matplotlib.pyplot as plt

def findjoint(joint_name, joint_list):
    i = 0
    for temp_joint in joint_list:
        #print temp_joint
        if temp_joint[0]==joint_name:
            return (joint_list[i][1], joint_list[i][2])
        else:
            i=i+1
if __name__ == '__main__':
    t0 = time()
    image_list = open("patchlist.txt")
    annotation = open("./imgs/annotation.txt")
    i = 0
    lines_list = [('htop','hbot'),('hbot','lsho'),('lsho','lelb'),('lelb','lwr'),('hbot','rsho'),('relb','rsho'),('relb','rwr'),('lsho','lhip'),('rsho','rhip'),('lhip','lkne'),('lkne','lank'),('rhip','rkne'),('rkne','rank')]
    for image_file in image_list:
        joint_list = []
        image_file =  image_file.rstrip()
        im = Image.open(image_file)
        width = im.size[0]
        height = im.size[1]
        plt.gca().set_aspect('equal', adjustable='box')
        plt.ylim(0, height)      
        plt.xlim(0, width)   
        plt.xlabel("image width")
        plt.ylabel("image height")
        plt.title("Skeleton plotting")  
        i=i+1
        line = annotation.readline()
        while line.split():
            str_class, str_x, str_y = line.split()
            #print image_file, str_class, str_x, str_y
            x = int(round(float(str_x)))
            y = height - int(round(float(str_y)))
            plt.plot([x],[y],'ro')
            joint_list.append((str_class,x,y))
            line = annotation.readline()
        #draw lines between joints
        for drawline in lines_list:
            point1 = findjoint(drawline[0], joint_list)
            point2 = findjoint(drawline[1], joint_list)
            plt.plot([point1[0],point2[0]],[point1[1],point2[1]],linewidth=2.0)
        plt.savefig('./imgs/matplot/'+str(i)+'.jpg', dpi=150)
        plt.clf()
    dt = time() - t0
    print 'done in %.2fs.' % dt
