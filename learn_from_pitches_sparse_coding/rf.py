#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

training_label = []
training_data = []
predict_label = []
predict_data = []
num = 0
num_epoches = 1

file = open( './feature.txt' , 'r' )
count = 0
for line in file :
    count+=1
    if count%100 == 0:
        print "read lines:", count
    line = line.rstrip()
    node = []
    label = re.search( r'^(.*?)\s', line ).group(1)
    #print label
    for i in range(1,300) :
        try :
            pattern = r'%s' % ( str( i ) + ':(.*?\s)' )
            match = re.search( pattern, line ).group(1)
            if match is None :
                node.append(0)
            else:
                node.append(match)
        except AttributeError :
            node.append(0)
            continue
    
    if num % 5 == 0 :
        predict_data.append( node )
        predict_label.append( label )
    else :
        training_data.append( node )
        training_label.append( label )
    num = num + 1

model = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=-1, random_state=None, verbose=0)

#model = svm.libsvm.fit( np.array( training_data,dtype=np.float64), np.array( training_label,dtype=np.float64), kernel='linear' )
for epoch in xrange(num_epoches):
    print "learning epoch: ", epoch, "/", num_epoches
    model.fit(training_data, training_label)
print "testing..."
output = model.predict(predict_data)
#output = svm.libsvm.predict( np.array( predict_data, dtype=np.float64), *model,  **{'kernel' : 'linear'} )
accurate_num = 0.0
for i in range( 0,len( output ) ) :
    if( int( predict_label[i] ) == int( output[i] ) ):
        accurate_num+=1
print "accuracy: ", accurate_num/len( output )
