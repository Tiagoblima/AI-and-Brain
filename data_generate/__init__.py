from random import *

from typing import List


def data_generate():
    ##Simulation with random numbers

    features_train = [[1, 30], [1, 24],[1, 86],[1,219],[2,34],[2,63]]  # type:List[List[int]]
    labels_train = [0,1,1,1,0,1]
    # for i in range(4000):
    #  x = randrange(0, 4)
    #  y = randrange(0, 4)
    #    coordnate = [x, y]
    #   features_train.append(coordnate)
    #    if (x == 1 & y == 3) | (x == 2 & y > 1) | (x == 3 & y > 1):
    #       labels_train.append(1)
    #    else:
    #        labels_train.append(0)

    features_test = [[3, 3],[2,62],[3,23],[3,19]]  # type: List[List[int]]
    labels_test = [0,1,0,0]

    #for i in range(2000):
     #   x = randrange(0, 6)
     #   y = randrange(0, 6)
     #  coordnate = [x, y]
     # features_test.append(coordnate)
     #   if (x == 1 & y == 3) | (x == 2 & y > 1) | (x == 3 & y > 1):
      #      labels_test.append(1)
      #  else:
       #     labels_test.append(0) "


    return features_train, features_test, labels_train,labels_test
