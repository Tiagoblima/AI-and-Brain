
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from data_generate import data_generate


features_train, features_test, labels_train, labels_test = data_generate()
good_grade = [features_train[ii][1] for ii in range(0,len(features_train)) if labels_train[ii] == 1]
high_level = [features_train[ii][0] for ii in range(0,len(features_train)) if labels_train[ii] == 1]
bad_grade =  [features_train[ii][1] for ii in range(0,len(features_train)) if labels_train[ii] == 0]
low_level =  [features_train[ii][0]  for ii in range(0,len(features_train)) if labels_train[ii] == 0]


plt.xlim(1, 4)
plt.ylim(0, 1)
plt.ylabel('Percentege of hits')
plt.xlabel('Level task')


plt.scatter(high_level,good_grade,c='b')
plt.scatter(low_level,bad_grade,c='r')
plt.axis([1, 4,0,1])
plt.show();

clf = SVC(kernel="rbf")
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)

acc = accuracy_score(labels_test,pred)
print "Accuracy: {0}".format(acc)
