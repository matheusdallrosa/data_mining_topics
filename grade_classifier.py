import sys

import numpy as np
from sklearn import tree

reputation = {'"home"':1,'"reputation"':2,'"course"':3,'"other"':4}

def convert_float(data):
    if type(data) == float or type(data) == int: return data
    if data == '"U"' or data == '"T"' or data == '"no"': return 0
    if data == '"R"' or data == '"A"' or data == '"yes"': return 1
    if data in reputation: return reputation[data]
    return data

base = []
for row in sys.stdin:
    base.append(row)

useless_features = [0,1,4,8,9,11]
features, targets = [], []

check_train = 0
test_idx = {1,51,101,151,201,251,301,351,401,451,501,551,601}
test_features, test_targets = [], []
for student in base:
    #to check if this student is for tests.
    check_train += 1
    #the input row came from a csv file.
    student_info = student.split(';')

    #features of the given student.
    usefull_features_str = np.delete(student_info[:30],useless_features)
    usefull_features_numeric = []
    for f in usefull_features_str:        
        usefull_features_numeric.append(convert_float(f)) 
    
    if check_train in test_idx:
        test_features.append(usefull_features_numeric)
        test_targets.append(student_info[32])
    else:
        features.append(usefull_features_numeric)

        #grades of the given student.
        #for g in student_info[30:33]:
        #  print(g)
        #  targets.append(float(g.split('"')[1]))

        #first we'll focus on the final grade.
        targets.append(student_info[32])

clf = tree.DecisionTreeClassifier()
clf.fit(features,targets)
print(clf.score(test_features,test_targets))
print(test_targets)
print(clf.predict(test_features,test_targets))