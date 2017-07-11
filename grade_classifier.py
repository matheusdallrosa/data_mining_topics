import sys

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

train_features = []
train_targets = []
with open(sys.argv[1]) as f:
    for row in f:
        info = row.split(';')
        train_targets.append(info[32])
        train_features.append(info[:30])        

max_score = 0
max_score_features = []
for i in range(0,30):
    for j in range(i+1,30):    
        for k in range(j+1,30):
            for l in range(k+1,30):
                for m in range(l+1,30):
        #            for n in range(m+1,30):                                                                                              
                    usefull_train_features = []     
                    for student_info in train_features:                                                    
                        usefull_train_features.append(np.take(student_info[:30],[i,j,k,l,m]))                            

                    clf = DecisionTreeClassifier(random_state=1000000007,min_samples_split=2)
                    score = max(cross_val_score(clf, usefull_train_features, train_targets, cv=10))*100
                    
                    if score > max_score:
                        max_score = score
                        max_score_features = [i,j,k,l,m]
    print(str(max_score))                    
    print(max_score_features)
print(max_score)
print(max_score_features)