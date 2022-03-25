def i_s_ps(schools, students):
    """
    Returns a table that gives for each pair (i, s) the p such as i = i^(s, p).
    """
    I = len(students)
    res = []
    for s in range(len(schools)):
        line = {}
        for i in range(I):
            line[schools[s].prefer[i]] = I - i
        res.append(line)
    return res




def demand(studs, table, s, P):
    """
    Returns the demand set for the school s using the table defined above.
    """
    res = []
    m = len(table)
    for i in range(len(table[0])):
        if table[s][studs[i]] >= P[s]:
            if studs[i].prefStud[s] < studs[i].prefStud[studs[i].schlStud]:
                for s_prime in range(m):
                    if table[s_prime][studs[i]] >= P[s] and studs[i].prefStud[s] > studs[i].prefStud[s_prime]:
                        break
                else:
                    res.append(i)
    return res




def T(P, res, studs, schools, table, feasibility):
    """
    Defines the T operation.
    feasibility is a function.
    """
    test = False
    I = len(studs)
    for s in range(len(table)):
        if res[s][0]:
            if P[s] == I + 1: continue
            res[s][1] = demand(studs, table, s, P)
            if not feasibility(schools[s], res[s][1], studs):
                P[s] += 1
                test = True
            else:
                res[s][0] = False
    return test




def fixed_algo(studs, schools, feasibility):
    """
    Runs the T operation until it finds a fixed point.
    We will use the observation that once we find a feasible demand for a
    school, it will be the demand returned by the algorithm.
    """
    table = i_s_ps(schools, studs)
    res = [[True, None] for s in range(len(schools))]
    P = [1] * len(schools)
    while T(P, res, studs, schools, table, feasibility):
        continue
    return [res[s][1] for s in range(len(schools))]