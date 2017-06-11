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

features, targets = [], []
useless_features = [0,1,4,8,9,11]
for student in sys.stdin:
    student_info = student.split(';')

    #features of the given student.
    usefull_features_str = np.delete(student_info[:30],useless_features)
    usefull_features_numeric = []
    for f in usefull_features_str:        
        usefull_features_numeric.append(convert_float(f)) 
    features.append(usefull_features_numeric)
    
    #grades of the given student.
    #for g in student_info[30:33]:
    #  print(g)
    #  targets.append(float(g.split('"')[1]))

    #first we'll focus on the final grade.
    targets.append(student_info[32])

clf = tree.DecisionTreeClassifier()
clf.fit(features,targets)
print(clf.score(features,targets))