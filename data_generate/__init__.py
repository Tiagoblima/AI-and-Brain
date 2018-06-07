from random import *

from typing import List


def data_generate():
    ##Simulation with random numbers

    features_train = [[1, 0.5]]  # type:
    labels_train = [1]

    for i in range(400):

        x = randrange(0, 41).__float__()/10

        qtd = randrange(10, 101)
        hit = randrange(0, qtd + 1)
        y = hit.__float__() / qtd.__float__()
        features_train.append([x, y])

        if x <= 1:
            if y > 0.7:
                labels_train.append(1)
            else:
                labels_train.append(0)
        elif x <= 2.0:
            if y > 0.6:
                labels_train.append(1)
            else:
                labels_train.append(0)
        elif x > 2.0:
            if y > 0.4:
                labels_train.append(1)
            else:
                labels_train.append(0)


    features_test = [[3, 0.9]]  # type: List[List[int]]
    labels_test = [0]

    for i in range(50):

        x = randrange(1, 4)

        qtd = randrange(10, 300)
        hit = randrange(0, qtd + 1)
        y = hit.__float__() / qtd.__float__()
        features_test.append([x, y])

        if x == 1:
            if y > 0.7:
                labels_test.append(1)
            else:
                labels_test.append(0)
        elif x == 2:
            if y > 0.6:
                labels_test.append(1)
            else:
                labels_test.append(0)
        elif x == 3:
            if y > 0.5:
                labels_test.append(1)
            else:
                labels_test.append(0)


    return features_train, features_test, labels_train, labels_test
