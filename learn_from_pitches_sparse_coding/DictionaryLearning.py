import Image
import ImageOps
import numpy as np
from time import time
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.decomposition import DictionaryLearning
#read the image list
def ImageListFile2Array(filename):
    patch_size = (8,8)
    stride_size = (6,6)
    imgArray = None
    image_list = open(filename)
    for image_file in image_list:
        #delete the enter space
        image_file =  image_file.rstrip()
        print image_file

        #read images
        im = Image.open(image_file)

        #convert to grayscal
        gray_im = ImageOps.grayscale(im)

        w = gray_im.size[0] - patch_size[0]
        h = gray_im.size[1] - patch_size[1]
        y = 0
        while y <= h:
            x = 0
            while x <= w:
                box = (x,y,x+patch_size[0],y+patch_size[1])
                crop_im = gray_im.crop(box)

                data = np.asarray(crop_im)
                data = data.reshape(1,data.size)
                if imgArray is None:
                    imgArray = data
                else:
                    imgArray = np.vstack((imgArray, data))
                x+=stride_size[0]
            y+=stride_size[1]
    return imgArray

#
num_basis = 100

#read the image list
imgArray = ImageListFile2Array('patchlist.txt')
print imgArray.shape
# initialize the dictionary class
print 'Learning the dictionary... '
t0 = time()
dico = MiniBatchDictionaryLearning(n_components=num_basis, alpha=1.0, transform_algorithm = 'lasso_lars', transform_alpha=1.0, fit_algorithm = 'lars', n_iter=100000)
#dico = DictionaryLearning(n_components=num_basis, alpha=1.0, transform_algorithm = 'lasso_lars', transform_alpha=1.0, fit_algorithm = 'lars', max_iter=500)

#set the average to 0, Standard deviation to 1 whitening
M = np.mean(imgArray, axis = 0)[np.newaxis,:]
whiteArray = imgArray - M
whiteArray /= np.std(whiteArray, axis = 0)

#compute the dictionary
V = dico.fit(whiteArray).components_

#print the processing time
dt = time() - t0
print 'done in %.2fs.' % dt

#save the dictionary
np.save('Dictionaries.npy', V)
