#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import numpy as np
from sklearn.datasets import svmlight_format
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    num_epoches = 10
    Train= svmlight_format.load_svmlight_file('./feature_train.txt')
    Test = svmlight_format.load_svmlight_file('./feature_test.txt')
    #method-0
#    model = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0)
    
    #method-1
    model = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None)

    #method-2
    #model = svm.libsvm.fit( np.array( training_data,dtype=np.float64), np.array( training_label,dtype=np.float64), kernel='linear' )
    for epoch in xrange(num_epoches):
        print "learning epoch: ", epoch, "/", num_epoches
        #method-0
#        model.fit( Train[0].toarray(), Train[1] )
        
        #method-1
        model.fit( Train[0], Train[1] )
    print "testing..."
    #output = model.predict(predict_data)
    
    #method-0
#    output = model.predict( Test[0].toarray() )
    
    #method-1
    output = model.predict( Test[0] )
    
    #output = svm.libsvm.predict( np.array( predict_data, dtype=np.float64), *model,  **{'kernel' : 'linear'} )
    accurate_num = 0.0
    for i in range( 0, len( output ) ) :
        if( int( Test[1][i] ) == int( output[i] ) ):
            accurate_num+=1
    print "accuracy: ", accurate_num/len( output )