class student2:
    """Definition of the class student"""

    def __init__(self, prefStud):
        """
        prefStud is a list that associates to each school its rank for the student.
        A case is added for including the choice of not joining any school at all.
        """
        self.prefStud = prefStud
        self.schlStud = len(prefStud) - 1

class school2:
    """Definition of the school class"""
    idx = 0
    n = 0
    def __init__(self, prefer, quota):
        """
        prefer contains the students ordered according to the preference of the school.
        """
        self.prefer = prefer
        self.quota = quota




def mate2(schools, students):
    N = len(students)
    m = len(schools)
    i = -1
     # since the algorithm goes through the preferences of the schools in decreasing order of
     # preference, we have a stable matching when all quotas are met.
    while True:
        for j in range(m):
            if schools[j].n < schools[j].quota and schools[i].idx < N:
                i = j
                break
        else:
            break
        while schools[i].n < schools[i].quota and schools[i].idx < N:
            stud = schools[i].prefer[schools[i].idx]
            if stud.prefStud[i] < stud.prefStud[stud.schlStud]:
                if stud.schlStud < m:
                    schools[stud.schlStud].n -= 1
                schools[i].n += 1
                stud.schlStud = i
            schools[i].idx += 1
    res = [list() for k in range(m + 1)]
    for k in range(N):
        res[students[k].schlStud].append(k)
    return res