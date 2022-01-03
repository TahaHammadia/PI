# You can install pulp using the command: pip install -U pulp

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0, cat="Integer")
y = LpVariable(name="y", lowBound=0, cat="Integer")

constraint = 2 * x + 4 * y >= 8

model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# Add the objective function to the model
model += x + 2 * y

# Add the objective function to the model
#model += lpSum([x, 2 * y])

# Solve the problem
status = model.solve()

for var in model.variables():
    print(f"{var.name}: {var.value()}")

def optimize(w, p, Ws):
    """
    w is the list of costs of the different groups.
    p is the list of the proportions of different groups.
    Ws is the budget of the school.
    """
    pass