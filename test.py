
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from data_generate import data_generate
from picture import prettyPicture

features_train, features_test, labels_train, labels_test = data_generate()
plt.xlim(0,5)
plt.ylim(0,5)

high_level = [features_train[ii][0] for ii in range(0,len(features_train))if labels_train==1]
good_average = [features_train[ii][0] for ii in range(0,len(features_train))if labels_train==1]
low_level = [features_train[ii][0] for ii in range(0,len(features_train))if labels_train==1]
bad_avarege = [features_train[ii][0] for ii in range(0,len(features_train))if labels_train==1]
plt.scatter(high_level,good_average,color="b",label="Good Average")
plt.scatter(low_level,bad_avarege,color="r",label="Bad Avarege")
plt.legend()
plt.xlabel("Level")
plt.ylabel("Averege")
plt.show()

clf = SVC()
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)

print pred

acc = accuracy_score(labels_test,pred)
print acc

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
