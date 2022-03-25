from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task04 import *
from Task07 import fixed_algo
import matplotlib.pyplot as plt

def feasability9(school, students, studsInfo):
    """
    feasability tests if the group quotas and the total quota are met.
    students is the list of proposed students.
    studsInfo is the list of all students which helps get data on them.
    """
    if len(students) > school.quota: return False
    cpt = [0] * len(school.quota_grp)
    for elt in students:
        if cpt[studsInfo[elt].grp] >= school.quota_grp[studsInfo[elt].grp]:
            return False
        cpt[studsInfo[elt].grp] += 1
    return True


# ### Test Instance 1:

def test9_1():
    """
    Shows a plot associating each student to a school.
    This function tests for the algorithm of part 4 with the group quotas constraint.
    """
    stud1 = student3([1, 2, 3], 0)
    stud2 = student3([2, 1, 3], 0)
    stud3 = student3([1, 3, 2], 0)
    stud4 = student3([3, 1, 2], 1)

    s1 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])
    s2 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])

    represent(fixed_algo([stud1, stud2, stud3, stud4], [s1, s2], feasability9) + [[]], ['r', 'b', 'g', 'y'])



# ### Test Instance 2:


def analyse9_2(n, rand_inst):
    """
    Returns the number of students from classes A, and B to get their first choice when we use the algorithm of part 4 with the group quotas constraint.
    """
    res = fixed_algo(rand_inst[1], rand_inst[0], feasability9)
    cptA, cptB = 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                else: cptB += 1
    return n, cptA, cptB




def printAnalyse9_2(n):
    """
    Prints the average number of students who get their first choice and their percentages for each group of instance 2. This tests for the algorithm of part 4 with the group quotas constraint.
    """
    m = int(9 * n / 10)
    N = 200

    cpta, cptb = 0, 0

    for _ in range(N):
        rand_inst = rand_instance2(n)
        n, cptA, cptB = analyse9_2(n, rand_inst)
        cpta += cptA
        cptb += cptB
    print(n, ":")
    print("Average of cptA:", cpta / N)
    print("Percentage of A's to get their first choice:", int(cpta / m / N * 10000) / 100, "%")
    print("Average of cptB : ", cptb / N)
    print("Percentage of B's to get their first choice:", int(cptb / (n - m) / N * 10000) / 100, "%")
    print("_______")




def test9_2():

    printAnalyse9_2(200)
    printAnalyse9_2(300)
    printAnalyse9_2(400)



# ### Test Instance 3:



def analyse9_3(n, rand_inst):
    """
    Returns the number of students from classes A, B, C and D to get their first choice when we use the algorithm of part 4 with the group quotas constraint.
    """
    res = fixed_algo(rand_inst[1], rand_inst[0], feasability9)
    cptA, cptB, cptC, cptD = 0, 0, 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                elif rand_inst[1][elt].grp == 1: cptB += 1
                elif rand_inst[1][elt].grp == 2: cptC += 1
                else: cptD += 1
    return n, cptA, cptB, cptC, cptD




def printAnalyse9_3(n):
    """
    Prints the average number of students who get their first choice and their percentages for each group of instance 3. This tests for the algorithm of part 4 with the group quotas constraint.
    """
    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    N = 200

    cpta, cptb, cptc, cptd = 0, 0, 0, 0

    for _ in range(N):
        rand_inst = rand_instance3(n)
        n, cptA, cptB, cptC, cptD = analyse9_3(n, rand_inst)
        cpta += cptA
        cptb += cptB
        cptc += cptC
        cptd += cptD
    print(n, ":")
    print("Average of cptA:", cpta / N)
    print("Percentage of A's to get their first choice:", int(cpta / m1 / N * 10000) / 100, "%")
    print("_______")
    print("Average of cptB : ", cptb / N)
    print("Percentage of B's to get their first choice:", int(cptb / (m2 - m1) / N * 10000) / 100, "%")
    print("_______")
    print("Average of cptC : ", cptc / N)
    print("Percentage of C's to get their first choice:", int(cptc / (m3 - m2) / N * 10000) / 100, "%")
    print("_______")
    print("Average of cptD : ", cptd / N)
    print("Percentage of D's to get their first choice:", int(cptd / (n - m3) / N * 10000) / 100, "%")
    print("_______")



def test9_3():

    printAnalyse9_3(200)
    printAnalyse9_3(300)
    printAnalyse9_3(400)