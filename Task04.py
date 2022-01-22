from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
import matplotlib.pyplot as plt
from random import gauss, random
from math import sqrt


def transf(match):
    res = [], []
    for i in range(len(match) - 1):
        for stud in match[i]:
            res[0].append(stud)
            res[1].append(i)
    return res

def represent(match, col):
    res = transf(match)
    plt.scatter(res[0], res[1], c = col)
    plt.title("Matching of students to schools")
    plt.xlabel("Student")
    plt.ylabel("School")
    plt.show()
    plt.close()


# ### Test Instance 1:

# #### Test Task 2:

def test1_2():

    stud1 = student2([1, 2, 3])
    stud2 = student2([2, 1, 3])
    stud3 = student2([1, 3, 2])
    stud4 = student2([3, 1, 2])

    s1 = school2([stud4, stud3, stud2, stud1], 2)
    s2 = school2([stud4, stud3, stud2, stud1], 2)

    represent(mate2([s1, s2], [stud1, stud2, stud3, stud4]), ['r', 'b', 'g', 'y'])


# #### Test Task 3:

def test1_3():

    stud1 = student3([1, 2, 3], 0)
    stud2 = student3([2, 1, 3], 0)
    stud3 = student3([1, 3, 2], 0)
    stud4 = student3([3, 1, 2], 1)

    s1 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])
    s2 = school3([stud4, stud3, stud2, stud1], 2, [2, 2])

    represent(mate3([s1, s2], [stud1, stud2, stud3, stud4]), ['r', 'b', 'g', 'y'])


# ### Test instance 2:




def app(studs, grp):
    s = random()
    if s >= 0.5 : choice = [1, 2]
    else: choice = [2, 1]
    studs.append(student3(choice, grp))

def rand_instance2(n):
    """
    mate2 works with arguments of the classes school3 and student3.
    """
    studs = []
    ranQty = []
    m = int(9 * n / 10)
    for k in range(m + 1):
        app(studs, 0)
        ranQty.append((k, gauss(0, 1)))
    for k in range(m + 1, n):
        app(studs, 1)
        ranQty.append((k, gauss(0, 1)))
    ranQty1 = [(k, ranQty[k][1] + gauss(0, 1)) for k in range(n)]
    ranQty2 = [(k, ranQty[k][1] + gauss(0, 1)) for k in range(n)]

    ranQty1.sort(key = lambda x : -x[1]) # decreasing order of observed quality
    ranQty2.sort(key = lambda x : -x[1])

    s1 = school3([studs[elt[0]] for elt in ranQty1], n // 4, [int(0.9 * n / 4), int(0.9 * n / 4)])
    s2 = school3([studs[elt[0]] for elt in ranQty2], n // 4, [int(0.9 * n / 4), int(0.9 * n / 4)])

    return [s1, s2], studs

def analyse2_2(n, rand_inst):
    res = mate2(rand_inst[0], rand_inst[1])
    cptA, cptB = 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                else: cptB += 1
    return n, cptA, cptB


def analyse2_3(n, rand_inst):
    res = mate3(rand_inst[0], rand_inst[1])
    cptA, cptB = 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                else: cptB += 1
    return n, cptA, cptB


# #### Test Task 2:



def printAnalyse2_2(n):
    m = int(9 * n / 10)
    N = 200

    cpta, cptb = 0, 0

    for _ in range(N):
        rand_inst = rand_instance2(n)
        n, cptA, cptB = analyse2_2(n, rand_inst)
        cpta += cptA
        cptb += cptB
    print(n, ":")
    print("Average of cptA:", cpta / N)
    print("Percentage of A's to get their first choice:", int(cpta / m / N * 10000) / 100, "%")
    print("Average of cptB : ", cptb / N)
    print("Percentage of B's to get their first choice:", int(cptb / (n - m) / N * 10000) / 100, "%")
    print("_______")



def test2_2():
    printAnalyse2_2(1000)
    printAnalyse2_2(2000)
    printAnalyse2_2(3000)


# The fraction of people getting their first choices seems independent from the number n or their class. Nearly three fourths of students get their first choice.

# #### Test Task 3:



def printAnalyse2_3(n):
    m = int(9 * n / 10)
    N = 200

    cpta, cptb = 0, 0

    for _ in range(N):
        rand_inst = rand_instance2(n)
        n, cptA, cptB = analyse2_3(n, rand_inst)
        cpta += cptA
        cptb += cptB
    print(n, ":")
    print("Average of cptA:", cpta / N)
    print("Percentage of A's to get their first choice:", int(cpta / m / N * 10000) / 100, "%")
    print("Average of cptB : ", cptb / N)
    print("Percentage of B's to get their first choice:", int(cptb / (n - m) / N * 10000) / 100, "%")
    print("_______")



def test2_3():
    printAnalyse2_3(1000)
    printAnalyse2_3(2000)
    printAnalyse2_3(3000)


# The fraction of people getting their first choices seems independent from the number n or their class. Nearly three fourths of students get their first choice.

# ### Test instance 3:




def app(studs, grp):
    s = random()
    if s >= 0.5 : choice = [1, 2]
    else: choice = [2, 1]
    studs.append(student3(choice, grp))

def rand_instance3(n):
    """
    mate2 works with arguments of the classes school3 and student3.
    """
    studs = []
    ranQty = []
    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    for k in range(m1 + 1):
        app(studs, 0)
        ranQty.append((k, gauss(0, 1)))
    for k in range(m1 + 1, m2 + 1):
        app(studs, 1)
        ranQty.append((k, gauss(0, 1)))
    for k in range(m2 + 1, m3 + 1):
        app(studs, 2)
        ranQty.append((k, gauss(0, 1)))
    for k in range(m3 + 1, n):
        app(studs, 3)
        ranQty.append((k, gauss(0, 1)))
    ranQty1 = [(k, ranQty[k][1] + gauss(0, 1)) for k in range(n)]
    ranQty2 = [(k, ranQty[k][1] + gauss(0, 1)) for k in range(n)]

    ranQty1.sort(key = lambda x : -x[1]) # decreasing order of observed quality
    ranQty2.sort(key = lambda x : -x[1])

    s1 = school3([studs[elt[0]] for elt in ranQty1], n // 4, [int(0.9 * n / 4), int(0.9 * n / 4), int(0.9 * n / 4), int(0.9 * n / 4)])
    s2 = school3([studs[elt[0]] for elt in ranQty2], n // 4, [int(0.9 * n / 4), int(0.9 * n / 4), int(0.9 * n / 4), int(0.9 * n / 4)])

    return [s1, s2], studs

def analyse3_2(n, rand_inst):
    res = mate2(rand_inst[0], rand_inst[1])
    cptA, cptB, cptC, cptD = 0, 0, 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                elif rand_inst[1][elt].grp == 1: cptB += 1
                elif rand_inst[1][elt].grp == 2: cptC += 1
                else: cptD += 1
    return n, cptA, cptB, cptC, cptD


def analyse3_3(n, rand_inst):
    res = mate3(rand_inst[0], rand_inst[1])
    cptA, cptB, cptC, cptD = 0, 0, 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                elif rand_inst[1][elt].grp == 1: cptB += 1
                elif rand_inst[1][elt].grp == 2: cptC += 1
                else: cptD += 1
    return n, cptA, cptB, cptC, cptD


# #### Test Task 2:



def printAnalyse3_2(n):
    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    N = 200

    cpta, cptb, cptc, cptd = 0, 0, 0, 0

    for _ in range(N):
        rand_inst = rand_instance3(n)
        n, cptA, cptB, cptC, cptD = analyse3_2(n, rand_inst)
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



def test3_2():
    printAnalyse3_2(1000)
    printAnalyse3_2(2000)
    printAnalyse3_2(3000)


# The fraction of people getting their first choices seems independent from the number n or their class. Nearly three fourths of students get their first choice.

# #### Test Task 3:




def printAnalyse3_3(n):
    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    N = 200

    cpta, cptb, cptc, cptd = 0, 0, 0, 0

    for _ in range(N):
        rand_inst = rand_instance3(n)
        n, cptA, cptB, cptC, cptD = analyse3_3(n, rand_inst)
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




def test3_3():
    printAnalyse3_3(1000)
    printAnalyse3_3(2000)
    printAnalyse3_3(3000)


# The fraction of people getting their first choices seems independent from the number n or their class. Nearly three fourths of students get their first choice.