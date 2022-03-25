from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task04 import *
from Task07 import fixed_algo
import matplotlib.pyplot as plt

def feasability10(school, students, studsInfo):
    """
    feasibility tests if the 4/5-rule is satisfied by the school.
    students is the list of proposed students.
    studsInfo is the list of all students which helps get data on them.
    """
    cpt = [0] * len(school.quota_grp)
    for elt in students:
        cpt[studsInfo[elt].grp] += 1
    for g in range(len(school.quota_grp)):
        if cpt[g] < 0.8 * school.quota_grp[g] or cpt[g] > 1.2 * school.quota_grp[g]:
            return False
    return True


# ### Test Instance 1:


def test10_1():
    """
    Shows a plot associating each student to a school.
    This function tests for the algorithm of part 4 with the 4/5-rule.
    """

    stud1 = student3([1, 2, 3], 0)
    stud2 = student3([2, 1, 3], 0)
    stud3 = student3([1, 3, 2], 0)
    stud4 = student3([3, 1, 2], 1)

    s1 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])
    s2 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])

    print(fixed_algo([stud1, stud2, stud3, stud4], [s1, s2], feasability10))


# ### Test Instance 2 and Instance 3:

def analyse10(n, rand_inst):
    """
    Returns if at most one student gets a school
    """
    P = fixed_algo(rand_inst[1], rand_inst[0], feasability10)
    temp = True
    for elt in P:
        if len(elt) not in [0, 1]:
            return False
        if temp and len(elt) == 1:
            temp = False
        elif len(elt) == 1: return False
    return True

# ### Test Instance 2:


def printAnalyse10_2(n):
    """
    Prints the result of the analyse10 for N = 200 trials with n students for instance 2.
    """
    N = 200
    cpt = 0
    for _ in range(N):
        rand_inst = rand_instance2(n)
        cpt += analyse10(n, rand_inst)
    print("n = ", n, "frac = ", cpt / N)

def test10_2():
    printAnalyse10_2(1000)


# ### Test Instance 3:

def printAnalyse10_3(n):
    """
    Prints the result of the analyse10 for N = 200 trials with n students for instance 3.
    """
    N = 200
    cpt = 0
    for _ in range(N):
        rand_inst = rand_instance3(n)
        cpt += analyse10(n, rand_inst)
    print("n = ", n, "frac = ", cpt / N)


def test10_3():
    printAnalyse10_3(1000)