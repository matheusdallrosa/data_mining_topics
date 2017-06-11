import sys

import numpy as np
from sklearn import tree

train_features = []
train_targets = []
with open(sys.argv[1]) as f:
    for row in f:
        info = row.split(';')
        train_targets.append(info[32])
        train_features.append(info[:30])        

test_features = []
test_targets = []
with open(sys.argv[2]) as f:
    for row in f:
        info = row.split(';')
        test_targets.append(info[32])
        test_features.append(info[:30])


max_score = 0
max_score_features = []
for i in range(0,30):
    for j in range(i+1,30):    
        for k in range(j+1,30):
            #for l in range(k+1,30):
            #    for m in range(l+1,30):
            #        for n in range(m+1,30):
                        #useless_features = [0,1,4,8,9,11]
                        
            useless_features = []
            for z in range(0,30):
                if z != i and z != j and z != k:# and z != l and z != m and z != n: 
                    useless_features.append(z)                        
                    
            usefull_train_features = []     
            for student_info in train_features:                                
                #features of the given student.
                usefull_features = np.delete(student_info[:30],useless_features)                            
                usefull_train_features.append(usefull_features)                            

            usefull_test_features = []
            for student_info in test_features:
                usefull_features = np.delete(student_info[:30],useless_features)
                usefull_test_features.append(usefull_features)                            

            clf = tree.DecisionTreeClassifier(random_state=1000000007,min_samples_split=2)
            clf.fit(usefull_train_features,train_targets)
            score = clf.score(usefull_test_features,test_targets)*100
            #print(str(i)+" "+str(score))
            if score > max_score:
                max_score = score
                max_score_features = [i,j,k]
            print(str(max_score))                    
print(max_score)
print(max_score_features)