from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task04 import *
import matplotlib.pyplot as plt

def feasability10(school, students, studsInfo):
    cpt = [0] * len(school.quota_grp)
    for elt in students:
        cpt[studsInfo[elt].grp] += 1
    for g in range(len(school.quota_grp)):
        if cpt[g] < 0.8 * school.quota_grp[g] or cpt[g] > 1.2 * school.quota_grp[g]:
            return False
    return True


# ### Test Instance 1:




stud1 = student3([1, 2, 3], 0)
stud2 = student3([2, 1, 3], 0)
stud3 = student3([1, 3, 2], 0)
stud4 = student3([3, 1, 2], 1)




s1 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])
s2 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])




fixed_algo([stud1, stud2, stud3, stud4], [s1, s2], feasability10)


# ### Test Instance 2:




def analyse10_2(n, rand_inst):
    P = fixed_algo(rand_inst[1], rand_inst[0], feasability10)
    for elt in P:
        if elt == len(rand_inst[1]) + 1:
            return True
    return False




def printAnalyse10_2(n):
    N = 200

    cpt = 0

    for _ in range(N):
        rand_inst = rand_instance2(n)
        cpt += analyse10_2(n, rand_inst)
    print("n = ", n, "frac = ", cpt / N)





printAnalyse10_2(1000)
printAnalyse10_2(2000)
printAnalyse10_2(3000)


# ### Test Instance 3:




def analyse10_3(n, rand_inst):
    P = fixed_algo(rand_inst[1], rand_inst[0], feasability10)
    for elt in P:
        if elt == len(rand_inst[1]) + 1:
            return True
    return False





def printAnalyse10_3(n):
    N = 200

    cpt = 0

    for _ in range(N):
        rand_inst = rand_instance3(n)
        cpt += analyse10_3(n, rand_inst)
    print("n = ", n, "frac = ", cpt / N)





printAnalyse10_3(1000)
printAnalyse10_3(2000)
printAnalyse10_3(3000)