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

    def __init__(self, group):
        self.group = group
        self.affected = False


def affect(N, G, schools, w):
    """
    N is the number of students which is supposed to be known
    G is the number of groups
    w is the column containing the costs of the different groups
    """

    cpt = N # cpt counts the number of students who do not have a school yet
    rank = 0

    while cpt > 0:
        for school in  schools:
            n = [0]*G
            n = np.array([[elt] for elt in n])
            students = []
            to_opt = False
            for stud in school.studs[rank]:
                if not stud.affected:
                    students.append(stud)
                    n[stud.group] += 1
                    to_opt = True

                if to_opt:
                    print("***|||**", w, n, school.Ws)
                    res = optimize(w, n, school.Ws)

            for stud in students:
                if res[stud.group] > 0:
                    stud.affected = True
                    cpt -= 1
                    res[stud.group] -= 1
                    school.prom.append(stud)
                    school.Ws -= w[stud.group,0]

student1 = student13(0)
student2 = student13(0)
student3 = student13(0)
student4 = student13(1)

w = np.array([[1], [10]])

G, N = 2, 4

s1 = school13([[student3, student1], [student2]], 11)
s2 = school13([[student4, student2], [student1]], 11)

schools = [s1, s2]

affect(N, G, schools, w)