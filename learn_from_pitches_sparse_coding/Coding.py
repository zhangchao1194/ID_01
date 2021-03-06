import Image
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import SparseCoder
from time import time
from multiprocessing import Pool

#Convert the gray scale array to RGB array
def GrayArray2RGB(gray_array):
    gray_shape = gray_array.shape
    rgb_data = np.zeros((gray_shape[0], gray_shape[1], 3), dtype=gray_array.dtype)
    for c in range(3):
        rgb_data[:,:,c] = gray_array[:,:,0]
    return rgb_data

def CodeCroppedImage(coder, data):
    u = coder.transform(data)
    #print u
    return u

def argwrapper(args):
    return args[0](*args[1:])

def maxpooling(array_for_pooling):
    maxarray = np.zeros( (array_for_pooling.shape[0]) )
    for y in xrange(array_for_pooling.shape[1]):
        for x in xrange(array_for_pooling.shape[2]):
            maxarray = np.maximum(maxarray, array_for_pooling[:,0,0])
            #print maxarray
    return maxarray


if __name__ == '__main__':
    t0 = time()
    func_args = []
    #input image
    src_file = '/root/git/repos/ID_01/learn_from_pitches_sparse_coding/imgs/articulations/hbot/1.jpg'
    cell_size = (8,8)
    pool_size = (2,2)
    stride_size = (2,2)

    V = np.load('./324 filters/Dictionaries(mini_8_8_6x6_100000).npy')
    im = Image.open(src_file)
    gray_im = ImageOps.grayscale(im)
    w = gray_im.size[0] - cell_size[0]
    h = gray_im.size[1] - cell_size[1]
    print "image size(pixel): ", w, h
    cell_w = (int)(gray_im.size[0]/cell_size[0])
    cell_h = (int)(gray_im.size[1]/cell_size[1])
    print "cell size(pixel): ", cell_size[0], cell_size[1]
    print "cell image size:(cell)", cell_w, cell_h
    print "pool size:(cell)", pool_size[0], pool_size[1]
    print "stride size(pool):", stride_size[0], stride_size[1]
    print "pooled image size:(pool)", int(cell_w/pool_size[0]), int(cell_h/pool_size[1])
    img_width = gray_im.size[0]
    img_height = gray_im.size[1]
    y = 0
    coder = SparseCoder(dictionary=V, transform_algorithm='omp', transform_n_nonzero_coefs=50)
#    dst_coded_array = np.zeros( (h_num_cell, w_num_cell*V.shape[0]) )

    #store all the cells
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
    #print len(func_args)
    p = Pool()
    list_results = p.map(argwrapper, func_args)
    array_reslts = np.asarray(list_results)
    array_reslts = array_reslts.transpose()  #324x416
    #temp = array_reslts[:,26]
    #print array_reslts.shape
    array_reslts.resize( (V.shape[0], cell_h, cell_w) ) #324x26x16
    #print array_reslts.shape
    #temp1 = array_reslts[:,0,1]
    #print np.array_equal(temp1, temp)

#on cell image
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
    pooled_array_results = pooled_array_results.reshape( (int(cell_h/pool_size[1]),int(cell_w/pool_size[0]),V.shape[0]) )
    np.save("train.npy",pooled_array_results)
    print "The size of array to be saved:", pooled_array_results.shape
    #compute the sparse coded vectors parallel
    dt = time() - t0
    print 'done in %.2fs.' % dt
