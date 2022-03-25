from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI/src"
# ad =
path.append(ad)

from Task11 import optimize
import numpy as np

class school13:

    def __init__(self, studs, Ws):
        """
        studs is the list of lists of students. Each list contains the students who have ranked the school at the i^th position. In the same group, the students who have classed less schools are prioritized in order to avoid the (|S| + 1)².
        """
        self.studs = studs
        self.Ws = Ws
        self.prom = []

class student13:

    def __init__(self, group, id = None):
        """
        id helps use represent
        """
        self.id = id
        self.group = group
        self.affected = False


def affect(N, G, schools, w):
    """
    Affects students to schools with our greedy algorithm.

    N is the number of students which is supposed to be known
    G is the number of groups
    w is the column containing the costs of the different groups

    The function acts directly on school13.prom. It returns also the loss value and the number of students who got a school.
    """

    cpt = N # cpt counts the number of students who do not have a school yet
    rank = 0
    loss = 0

    while cpt > 0 and rank < len(schools):

        for school in  schools:

            n = [0]*G
            n = np.array([[elt] for elt in n])
            students = []
            to_opt = False
            for stud in school.studs[rank]:
            # we work on the students ranking a given school at the rank position
                if not stud.affected:
                    students.append(stud)
                    n[stud.group] += 1
                    to_opt = True
                    # we optimize when there are unaffected students ranking

                if to_opt:
                    res = optimize(w, n, school.Ws)

            for stud in students:
                if res[stud.group] > 0:
                    stud.affected = True
                    cpt -= 1 # adjust the count of students
                    loss += (1 + rank)**2 # adjust the loss
                    res[stud.group] -= 1 # adjust the count of groups
                    school.prom.append(stud) # add the student to the promotion
                    school.Ws -= w[stud.group,0] # update the budget constraint
        rank += 1
    loss += cpt * (len(schools) + 1) ** 2 # count the students who do not have a school
    return loss, N - cpt

