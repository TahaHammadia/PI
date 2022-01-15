import numpy as np
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

def optimize(w, p, Ws):
    """
    w is the list of costs of the different groups.
    p is the list of the proportions of different groups.
    Ws is the budget of the school.
    """
    G = len(p)
    model = LpProblem(name="Task_5.1", sense=LpMaximize)
    groups = np.array([[LpVariable(name="x" + str(i), lowBound=0, cat="Integer")] for i in range(G)]) # variables
    model += lpSum(groups) # objective function
    print(lpSum(groups))

    # Constraints
    cost = []
    for i in range(G):
        cost.append(w[i,0] * groups[i, 0])
    model += lpSum(cost) <= Ws
    print(lpSum(cost) <= Ws)

    A1 = np.array([[6 / 5 * p[i, 0]] * G for i in range(G)])
    A2 = np.array([[-4 / 5 * p[i, 0]] * G for i in range(G)])
    for i in range(G):
        A1[i, i] -= 1
        A2[i, i] += 1

    set1 = A1.dot(groups)
    set2 = A2.dot(groups)

    for i in range(G):
        model += set1[i, 0] >= 0
        print(set1[i, 0] >= 0)
        model += set2[i, 0] >= 0
        print(set2[i, 0] >= 0)

    status = model.solve()

    for var in model.variables():
        print(f"{var.name}: {var.value()}")

w = np.array([[1], [10]])
p = np.array([[3/4], [1/4]])
Ws = 11
optimize(w, p, Ws)