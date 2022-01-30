class student3:
    """Definition of the class student"""

    def __init__(self, prefStud, grp):
        """
        prefStud is a list that associates to each school its rank for the student.
        A case is added for including the choice of not joining any school at all.
        """
        self.prefStud = prefStud
        self.schlStud = len(prefStud) - 1
        self.grp = grp

class school3:
    """Definition of the school class"""
    idx = 0
    n = 0
    def __init__(self, prefer, quota, quota_grp):
        """
        prefer contains the students ordered according to the preference of the school.
        """
        self.prefer = prefer
        self.quota = quota
        self.quota_grp = quota_grp
        self.n_grp = [0] * len(quota_grp)




def mate3(schools, students):
    """
    Returns a list of lists [[...], ..., [...]]. Each list contains a list of the NUMBER of the students that attend the corresponding school. The last list contains the NUMBERS of the students who do not get any school.
    """
    N = len(students)
    m = len(schools)
    i = -1
    while True:  # stop condition unmodified
        for j in range(m):
            if schools[j].n < schools[j].quota and schools[i].idx < N:
                i = j
                break
        else:
            break
        while schools[i].n < schools[i].quota and schools[i].idx < N:
            stud = schools[i].prefer[schools[i].idx]
            if schools[i].n_grp[stud.grp] < schools[i].quota_grp[stud.grp]:
                if stud.prefStud[i] < stud.prefStud[stud.schlStud]:
                    if stud.schlStud < m:
                        schools[stud.schlStud].n -= 1
                        schools[i].n_grp[stud.grp] -= 1
                    schools[i].n += 1
                    stud.schlStud = i
            schools[i].idx += 1

    # preparing the promised format
    res = [list() for k in range(m + 1)]
    for k in range(N):
        res[students[k].schlStud].append(k)
    return res