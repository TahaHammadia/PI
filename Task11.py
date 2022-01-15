import numpy as np
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

def optimize(w, n, Ws):
    """
    w is the list of costs of the different groups.
    n is the number of candidate students from each group.
    Ws is the budget of the school.
    """
    G = len(n)
    N = sum(n) # total number of all students
    p = np.array([n[i] / N for i in range(G)])
    model = LpProblem(name="Task_5.1", sense=LpMaximize)
    groups = np.array([[LpVariable(name="x" + str(i), lowBound=0, cat="Integer")] for i in range(G)]) # variables
    model += lpSum(groups) # objective function

    # #Constraints
    # Cost constraint
    cost = []
    for i in range(G):
        cost.append(w[i,0] * groups[i, 0])
    model += lpSum(cost) <= Ws

    # Number constraint
    for i in range(G):
        model += 1 * groups[i,0] <= n[i,0]

    #4/5- rule
    A1 = np.array([[6 / 5 * p[i, 0]] * G for i in range(G)])
    A2 = np.array([[-4 / 5 * p[i, 0]] * G for i in range(G)])
    for i in range(G):
        A1[i, i] -= 1
        A2[i, i] += 1

    set1 = A1.dot(groups)
    set2 = A2.dot(groups)

    for i in range(G):
        model += set1[i, 0] >= 0
        model += set2[i, 0] >= 0

    # Solution
    status = model.solve()

    for var in model.variables():
        print(f"{var.name}: {var.value()}")

w = np.array([[1], [10]])
n = np.array([[3], [1]])
Ws = 1000
optimize(w, n, Ws)