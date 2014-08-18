import Image
import ImageOps
import numpy as np
import os

def count_file_num(path):
    count = 0
    for root, dirs, files in os.walk(path):
        fileLength = len(files)
        if fileLength != 0:
            count = count + fileLength
    return count
    
if __name__ == '__main__':
    f = open("feature.txt","wr")
    str_class = ("lank","lkne","lhip","rhip","rkne","rank","lwr","lelb","lsho","rsho","relb","rwr","hbot","htop")
    for temp in str_class:
        filepath = "../imgs/articulations/" + temp + "/"
        count = count_file_num(filepath)
        class_int = str_class.index(temp)
        print (float(class_int)/14.0)*100, "%"
        j = 0
        for i in xrange(count):
            str_feature=str(class_int)+" "
            j = j+1
            imgpath = filepath + str(j) + ".jpg"
            img = Image.open(imgpath)
            gray_im = ImageOps.grayscale(img)
            feature = np.asarray(gray_im)
            feature = feature.reshape(1,feature.size)
            for axis in xrange(feature.shape[1]):
                if feature[0,axis]!=0:
                    str_feature = str_feature + str(axis) + ":" + str(feature[0,axis]) + " "
            str_feature += "\n"
            f.write(str_feature)
