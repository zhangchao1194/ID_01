import re
import numpy as np

file = open( './feature.txt' , 'r' )
file_train = open( './feature_train.txt' , 'w' )
file_test = open( './feature_test.txt' , 'w' )

num = 0
for line in file :
    if num % 5 == 0 :
        file_test.write(line)
    else :
        file_train.write(line)
    num = num + 1
