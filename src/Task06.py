from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task05 import *
from Task04 import rand_instance2, rand_instance3, represent
import matplotlib.pyplot as plt



# ### Test instance 1:

def test6_1():

    prop = [0.75, 0.25]

    stud1 = student3([1, 2, 3], 0)
    stud2 = student3([2, 1, 3], 0)
    stud3 = student3([1, 3, 2], 0)
    stud4 = student3([3, 1, 2], 1)

    s1 = school2([stud4, stud3, stud2, stud1], 2)
    s2 = school2([stud4, stud3, stud2, stud1], 2)

    fair_rank(s1.prefer, prop)
    fair_rank(s2.prefer, prop)

    represent(mate2([s1, s2], [stud1, stud2, stud3, stud4]), ['r', 'b', 'g', 'y'])


# #### Test instance 2 and 3:

def test(rand_inst,prop):
    """
    Determines whether the schools satisfie the 4/5-rule and returns the result in a list.
    """
    r = 0.8
    R = 1.2
    n = len(prop)
    res = mate2(rand_inst[0], rand_inst[1])
    ret = []
    for s in [0, 1]:
        cpt = [0] * n
        Ns = len(res[s])
        for elt in res[s]:
            cpt[rand_inst[1][elt].grp] += 1
        for i in range(n):
            if (cpt[i] - 1) / Ns < r or (cpt[i] + 1) / Ns > R:
                ret.append(False)
        ret.append(True)
    return ret




# ### Test instance 2:

prop2 = [0.9, 0.1]


def printAnalyse6_2(n):
    """
    Prints if the schools s1 and s2 satisfy the 4/5-rule for instance 2.
    """

    N = 200

    for _ in range(N):
        rand_inst = rand_instance2(n)
        fair_rank(rand_inst[0][0].prefer, prop2)
        fair_rank(rand_inst[0][1].prefer, prop2)
    boolean = test(rand_inst, prop2)
    print(n, ":")
    print("s1 verifies the 4/5 - rule ", boolean[0])
    print("s2 verifies the 4/5 - rule ", boolean[1])
    print("________________")




def test6_2():
    printAnalyse6_2(1000)
    printAnalyse6_2(1500)
    printAnalyse6_2(2000)



# ### Test instance 3:

prop3 = [0.5, 0.3, 0.15, 0.05]


def printAnalyse6_3(n):
    """
    Prints if the schools s1 and s2 satisfy the 4/5-rule for instance 3.
    """

    N = 200

    for _ in range(N):
        rand_inst = rand_instance3(n)
        fair_rank(rand_inst[0][0].prefer, prop3)
        fair_rank(rand_inst[0][1].prefer, prop3)
    boolean = test(rand_inst, prop3)
    print(n, ":")
    print("s1 verifies the 4/5 - rule ", boolean[0])
    print("s2 verifies the 4/5 - rule ", boolean[1])
    print("________________")



def test6_3():
    printAnalyse6_3(1000)
    printAnalyse6_3(1500)
    printAnalyse6_3(2000)