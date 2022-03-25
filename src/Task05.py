def fair_rank(L, prop):
    """
    Procedure that changes the preference list of a school.
    L is a list of ranked students from the most preferred school to the least preferred by the school.
    prop is the list of proportions of the groups in the population.
    Acts directly on the list of preferences.
    """
    r = 0.8
    R = 1.2
    n = len(prop) # number of groups
    N = len(L) # number of students
    cpt = [0] * n
    cpt[L[0].grp] = 1
    for k in range(1, len(L)):
        lim_inf = [False] * n
        lim_sup = [False] * n
        act = False
        for i in range(n):
            if cpt[i] / (k + 1) <= r * prop[i]:
                lim_inf[i] = True
                act = True
            if cpt[i] / (k + 1) >= R * prop[i]:
                lim_sup[i] = True
                act = True
        if act:
            for j in range(k, N):
                if lim_sup[L[j].grp]: continue
                if lim_inf[L[j].grp]:
                    temp = L[j]
                    for l in range(j-1, k-1, -1):
                        L[l + 1] = L[l]
                    L[k] = temp
                    break
        cpt[L[k].grp] += 1  # keeping track of the number of people of each group