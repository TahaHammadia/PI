from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task04 import *
import matplotlib.pyplot as plt

def feasability8(school, students, studsInfo):
    return school.quota >= len(students)


# ### Test Instance 1:



stud1 = student2([1, 2, 3])
stud2 = student2([2, 1, 3])
stud3 = student2([1, 3, 2])
stud4 = student2([3, 1, 2])




s1 = school2([stud4, stud3, stud2, stud1], 2)
s2 = school2([stud4, stud3, stud2, stud1], 2)




represent(fixed_algo([stud1, stud2, stud3, stud4], [s1, s2], feasability8) + [[]], ['r', 'b', 'g', 'y'])



# ### Test Instance 2:




def analyse8_2(n, rand_inst):
    res = fixed_algo(rand_inst[1], rand_inst[0], feasability8)
    cptA, cptB = 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                else: cptB += 1
    return n, cptA, cptB





def printAnalyse8_2(n):
    m = int(9 * n / 10)
    N = 200

    cpta, cptb = 0, 0

    for _ in range(N):
        rand_inst = rand_instance2(n)
        n, cptA, cptB = analyse8_2(n, rand_inst)
        cpta += cptA
        cptb += cptB
    print(n, ":")
    print("Average of cptA:", cpta / N)
    print("Percentage of A's to get their first choice:", int(cpta / m / N * 10000) / 100, "%")
    print("Average of cptB : ", cptb / N)
    print("Percentage of B's to get their first choice:", int(cptb / (n - m) / N * 10000) / 100, "%")
    print("_______")




printAnalyse8_2(1000)
printAnalyse8_2(2000)
printAnalyse8_2(3000)



# ### Test Instance 3:



def analyse8_3(n, rand_inst):
    res = fixed_algo(rand_inst[1], rand_inst[0], feasability8)
    cptA, cptB, cptC, cptD = 0, 0, 0, 0
    for s in [0, 1]:
        for elt in res[s]:
            if rand_inst[1][elt].prefStud[s] == 1:
                if rand_inst[1][elt].grp == 0: cptA += 1
                elif rand_inst[1][elt].grp == 1: cptB += 1
                elif rand_inst[1][elt].grp == 2: cptC += 1
                else: cptD += 1
    return n, cptA, cptB, cptC, cptD




def printAnalyse8_3(n):
    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    N = 200

    cpta, cptb, cptc, cptd = 0, 0, 0, 0

    for _ in range(N):
        rand_inst = rand_instance3(n)
        n, cptA, cptB, cptC, cptD = analyse8_3(n, rand_inst)
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




printAnalyse8_3(1000)
printAnalyse8_3(2000)
printAnalyse8_3(3000)