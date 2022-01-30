from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)

import numpy as np
from Task11 import optimize

import matplotlib.pyplot as plt

# ## Instance 1

def test12_1():
    w = np.array([[1], [10]]) # set of cost for each group

    n = np.array([[3], [1]]) # number of students per group
    Ws = 11                      # The budget for school s
    optimize(w, n, Ws)



# ## Instance 2

def instance2_5(n, p,w):

    G = len(p)
    n_studs = np.array([[int(n*p[i])] for i in range(G)])

    Ws = 3*n

    return optimize(w, n_studs,Ws )


def compute12_2():
    p = [0.9, 0.1]
    w = np.array([[1], [10]])
    res = []
    for k in range(22,51):
        res.append((k, instance2_5(k, p, w)))
    return res

def test12_2():

    results = compute12_2()
    x = [results[i][1][0] for i in range(len(results))]
    y = [results[i][1][1] for i in range(len(results))]
    bins = [results[i][0] for i in range(len(results))]
    plt.plot(bins, x, color='r')
    plt.plot(bins, y, color='g')
    plt.xlabel("Number of candidates")
    plt.ylabel("Number of students from each group")
    plt.title("Test for instance 2")
    plt.show()

# ## Instance 3

def instance3_5(n, p,w):

    G = len(p)
    n_studs = np.array([[int(n*p[i])] for i in range(G)])

    Ws = 3*n

    return optimize(w, n_studs,Ws)

def compute12_3():

    p = [0.5,0.3,0.15,0.05]
    res = []
    w = np.array([[1], [5], [6], [10]])

    for k in range(22,51):
        res.append((k, instance3_5(k, p, w)))
    return res

def test12_3():

    results = compute12_3()
    x = [results[i][1][0] for i in range(len(results))]
    y = [results[i][1][1] for i in range(len(results))]
    z = [results[i][1][2] for i in range(len(results))]
    u = [results[i][1][3] for i in range(len(results))]
    bins = [results[i][0] for i in range(len(results))]
    plt.plot(bins, x, bins, y, bins, z, bins, u)
    plt.xlabel("Number of candidates")
    plt.ylabel("Number of students from each group")
    plt.title("Test for instance 3")
    plt.show()
