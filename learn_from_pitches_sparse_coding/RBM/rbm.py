from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import BernoulliRBM
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.datasets import svmlight_format
import numpy as np
import argparse
import time
import cv2

def scale(X, eps = 0.001):
	# scale the data points s.t the columns of the feature space
	# (i.e the predictors) are within the range [0, 1]
	return (X - np.min(X, axis = 0)) / (np.max(X, axis = 0) + eps)
def nudge(X, y):
	# initialize the translations to shift the image one pixel
	# up, down, left, and right, then initialize the new data
	# matrix and targets
	translations = [(0, -1), (0, 1), (-1, 0), (1, 0)]
	data = []
	target = []

	# loop over each of the digits
	for (image, label) in zip(X, y):
		# reshape the image from a feature vector of 784 raw
		# pixel intensities to a 28x28 'image'
		image = image.reshape(28, 28)

		# loop over the translations
		for (tX, tY) in translations:
			# translate the image
			M = np.float32([[1, 0, tX], [0, 1, tY]])
			trans = cv2.warpAffine(image, M, (28, 28))

			# update the list of data and target
			data.append(trans.flatten())
			target.append(label)

	# return a tuple of the data matrix and targets
	return (np.array(data), np.array(target))
   	
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required = True,
	    help = "path of data set")
    ap.add_argument("-t", "--test", required = True, type = float,
	    help = "size of test split")
#    ap.add_argument("-s", "--search", type = int, default = 0,
#	    help = "whether or not a grid search should be performed")
    args = vars(ap.parse_args())
    
    X = svmlight_format.load_svmlight_file(args['dataset'])
#    Test = svmlight_format.load_svmlight_file(args['test_dataset'])
    XX = X[0].toarray()
    XX = XX.astype("float32")
    yy = X[1]
    XX = scale(XX) 
    (trainX, testX, trainY, testY) = train_test_split(XX, yy, test_size = args['test'], random_state = 42)
    print testX.shape
    	
