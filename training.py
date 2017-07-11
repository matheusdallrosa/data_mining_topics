import sys

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

usefull_features = []
for i in range(0,30):
    usefull_features.append(i)

train_targets = []
train_features = []
with open(sys.argv[1]) as f:
    for row in f:
        info = row.split(';')
        train_targets.append(info[32])
        train_features.append(np.take(info[:30],usefull_features))

clf = DecisionTreeClassifier(random_state=1000000007,min_samples_split=2)
scores = cross_val_score(clf, train_features, train_targets, cv = 10)
print(max(scores))
print(len(scores))