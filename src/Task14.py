from random import random
import numpy as np
import matplotlib.pyplot as plt

from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)
from Task04 import represent, rand_instance2, rand_instance3
from Task13 import *

# ## Instance 1

def test14_1():
    """
    Shows a plot associating each student to a school.
    This function tests our algorithm in task 13.
    """

    student1 = student13(0, 0)
    student2 = student13(0, 1)
    student3 = student13(0, 2)
    student4 = student13(1, 3)

    w = np.array([[1], [10]])

    G, N = 2, 4

    s1 = school13([[student3, student1], [student2]], 11)
    s2 = school13([[student4, student2], [student1]], 11)

    schools = [s1, s2]

    loss, n_prom = affect(N, G, schools, w)
    represent([[student.id for student in s.prom]for s in [s1,s2]] + [[]], ['r', 'b', 'g', 'y'][:n_prom])

    return loss


# ### Instance 2 and 3:

def app14(studs, grp, list_s1, list_s2):
    """
    Procedure that associates a student to a school randomly.
    Uses lists list_s1 and list_s2 in order to optimize the definition of s1 and s2.
    """

    s = random()
    if s >= 0.5 :
        stud = student13(grp)
        list_s1.append(stud)
    else:
        stud = student13(grp)
        list_s2.append(stud)
    studs.append(stud)

# ## Instance 2:

def rand_instance2_14(n):
    """
    Returns a random instance corresponding to instance 2.

    Since all the students rank both schools. No need to care about ranking the students within the i^th list.
    """
    studs = []
    list_s1 = []
    list_s2 = []

    ranQty = []
    m = int(9 * n / 10)
    for k in range(m + 1):
        app14(studs, 0, list_s1, list_s2)
    for k in range(m + 1, n):
        app14(studs, 1, list_s1, list_s2)

    s1 = school13([list_s1] + [list_s2], n)
    s2 = school13([list_s2] + [list_s1], n)

    return s1, s2

def test14_2():
    """
    Show the evolution of the penalty and the number of accepted students in function of the number of candidates for instance 2.
    """
    loss, n_prom, Res = [], [], []
    for n in range(10, 51):
        s1, s2 = rand_instance2_14(n)
        temp1, temp2 = affect(n, 2, [s1, s2], np.array([[1],[10]]))
        loss.append(temp1)
        n_prom.append(temp2)
    bins = [k for k in range(10, 51)]

    plt.plot(bins, loss)
    plt.xlabel("Number of candidates")
    plt.ylabel("Penalty value")
    plt.title("Test for instance 2")
    plt.show()

    plt.plot(bins, n_prom)
    plt.xlabel("Number of candidates")
    plt.ylabel("Number of students")
    plt.title("Test for instance 2")
    plt.show()

# ## Instance 3:

def rand_instance3_14(n):
    """
    Returns a random instance corresponding to instance 3.

    Since all the students rank both schools. No need to care about ranking the students within the i^th list.
    """

    studs = []
    list_s1 = []
    list_s2 = []

    m1 = n // 2
    m2 = int(4 * n / 5)
    m3 = int(19 * n / 20)
    for k in range(m1 + 1):
        app14(studs, 0, list_s1, list_s2)
    for k in range(m1 + 1, m2 + 1):
        app14(studs, 1, list_s1, list_s2)
    for k in range(m2 + 1, m3 + 1):
        app14(studs, 2, list_s1, list_s2)
    for k in range(m3 + 1, n):
        app14(studs, 3, list_s1, list_s2)

    s1 = school13([list_s1] + [list_s2], 3 * n)
    s2 = school13([list_s2] + [list_s1], 3 * n)

    return s1, s2

def test14_3():
    """
    Show the evolution of the penalty and the number of accepted students in function of the number of candidates for instance 3.
    """
    loss, n_prom = [], []
    for n in range(10, 51):
        s1, s2 = rand_instance3_14(n)
        temp1, temp2 = affect(n, 4, [s1, s2], np.array([[1],[5],[6],[10]]))
        loss.append(temp1)
        n_prom.append(temp2)
    bins = [k for k in range(10, 51)]

    plt.plot(bins, loss)
    plt.xlabel("Number of candidates")
    plt.ylabel("Penalty value")
    plt.title("Test for instance 3")
    plt.show()

    plt.plot(bins, n_prom)
    plt.xlabel("Number of candidates")
    plt.ylabel("Number of students")
    plt.title("Test for instance 3")
    plt.show()