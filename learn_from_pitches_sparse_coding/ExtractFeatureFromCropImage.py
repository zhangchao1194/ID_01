import Image
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import SparseCoder
from time import time
from multiprocessing import Pool
from sklearn.preprocessing import normalize
import os

def CodeCroppedImage(coder, data):
    u = coder.transform(data)
    #print u
    return u

def argwrapper(args):
    return args[0](*args[1:])

def maxpooling(array_for_pooling):
    maxarray = np.zeros( (array_for_pooling.shape[0]) )
#    maxarray_absolute = np.zeros( (array_for_pooling.shape[0]) )
    for y in xrange(array_for_pooling.shape[1]):
        for x in xrange(array_for_pooling.shape[2]):
#            maxarray_absolute = np.maximum(maxarray_absolute, np.absolute(array_for_pooling[:,0,0]))
            maxarray = np.maximum(maxarray, array_for_pooling[:,0,0])
#    for temp in xrange(maxarray.size):
#        if maxarray_absolute[temp]!=maxarray[temp]:
#            maxarray[temp] = 0-maxarray_absolute[temp]
    return maxarray

def count_file_num(path):
    count = 0
    for root, dirs, files in os.walk(path):
        fileLength = len(files)
        if fileLength != 0:
            count = count + fileLength
    return count

def crop_img_to_feature(color_img, p):
    V = np.load('./100 filters/Dictionaries(mini_8_8_6_6_100000).npy')
    func_args = []
    cell_size = (8,8)
    pool_size = (2,2)
    stride_size = (2,2)
    gray_im = ImageOps.grayscale(color_img)
    w = gray_im.size[0] - cell_size[0]
    h = gray_im.size[1] - cell_size[1]
    cell_w = (int)(gray_im.size[0]/cell_size[0])
    cell_h = (int)(gray_im.size[1]/cell_size[1])
    img_width = gray_im.size[0]
    img_height = gray_im.size[1]
    y = 0
    coder = SparseCoder(dictionary=V, transform_algorithm='lasso_lars', transform_n_nonzero_coefs=10)
    while y <= h:
        x = 0
        while x <= w:
            box = (x,y,x+cell_size[0],y+cell_size[1])
            crop_im = gray_im.crop(box)
            data = np.asarray(crop_im)
            data = data.reshape(1,data.size)
            func_args.append( (CodeCroppedImage,coder,data) )
            x+=cell_size[0]
        y+=cell_size[1]

    list_results = p.map(argwrapper, func_args)
    array_reslts = np.asarray(list_results)
    array_reslts = array_reslts.transpose()  #324x416
    array_reslts.resize( (V.shape[0], cell_h, cell_w) ) #324x26x16
    y = 0
    w = cell_w - pool_size[0]
    h = cell_h - pool_size[1]
    func_args = []
    while y <= h:
        x = 0
        while x <= w:
            array_for_pooling = array_reslts[:,y:y+pool_size[1],x:x+pool_size[0]]
            func_args.append( (maxpooling,array_for_pooling) )
            x+=pool_size[0]
        y+=pool_size[1]
    pooled_list_results = p.map(argwrapper, func_args)
    pooled_array_results = np.asarray(pooled_list_results)
    pooled_array_results = pooled_array_results.reshape( (1,1,V.shape[0]*pool_size[0]*pool_size[1]) )


    #print pooled_array_results.shape
    return pooled_array_results

def l2_normalize(feature):
    feature_2d = feature.reshape( (1,feature.shape[2]) )
    feature_2d = normalize(feature_2d, norm='l2', axis=1, copy=True)
    return feature_2d

if __name__ == '__main__':
    t0 = time()
    p = Pool()
    f = open("feature.txt","wr")
#    str_class = ("lank","lkne","lhip","rhip","rkne","rank","lwr","lelb","lsho","rsho","relb","rwr","hbot","htop","neg")
    str_class = ("lank","lkne","lhip","rhip","rkne","rank","lwr","lelb","lsho","rsho","relb","rwr","hbot","htop","neg")
    for temp in str_class:
        filepath = "./imgs/articulations/" + temp + "/"
        count = count_file_num(filepath)
        class_int = str_class.index(temp)
        print (float(class_int)/14.0)*100, "%"
        j = 0
        for i in xrange(count):
            str_feature=str(class_int)+" "
            j = j+1
            imgpath = filepath + str(j) + ".jpg"
            img = Image.open(imgpath)
            #extract feature
            feature = crop_img_to_feature(img,p)
            feature = l2_normalize(feature)
            for axis in xrange(feature.shape[1]):
                if feature[0,axis]!=0:
                    str_feature = str_feature + str(axis) + ":" + str(feature[0,axis]) + " "
            str_feature += "\n"
            f.write(str_feature)
            #raw_input()
            #write into file f

    dt = time() - t0
    print 'done in %.2fs.' % dt
