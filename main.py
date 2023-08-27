#imports
from pulp import *
import matplotlib.pyplot as plt
import numpy as np

#variables

Min = False
Max = True


# Define the objective function
x0,y0 = 3,4



#First constraint
x1,y1 = 1,1
# >= means
ls1 = None
#<= means 
gs1 =450



#Second constraint
x2,y2=2,1
# >= means
ls2 = None
#<= means 
gs2 =600






# Create the LP problem

if Max == True:
    prob = LpProblem("Linear Programming Problem", LpMaximize)
    
else:
    prob = LpProblem("Linear Programming Problem", LpMinimize)

# Define the decision variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Define the constraints


conrains = []

if ls1 != None:   
    conrains.append(ls1)
if ls2 != None:   
    conrains.append(ls2)
    
if gs1 != None:   
    conrains.append(gs1)
    
if gs2 != None:   
    conrains.append(gs2)   
    
if ls1 == None:   
    A = x1 * x + y1 * y <= gs1
else:
    A = x1 * x + y1 * y >= ls1


if ls2 == None:
    B = x2*x + y2* y <= gs2
else:
    B = x2*x + y2* y >= ls2

# Add the constraints to the problem
prob += A
prob += B
prob += x0 * x + y0 * y 
# Solve the LP problem
prob.solve()

# Print the results
print("Objective Function Value:", value(prob.objective))
print("x =", value(x))
print("y =", value(y))


largest_number = max(conrains)

# Plot the feasible region
if largest_number <=10 :
    x_values = np.linspace(0,10)
elif largest_number <=100 :
    x_values = np.linspace(0,100)
elif largest_number <=1000 :
    x_values = np.linspace(0,1000)
elif largest_number <=10000 :
    x_values = np.linspace(0,10000)    


   
y_values_1 = gs1-x1*x_values/y1
y_values_2 = (gs2 -x2* x_values)/y2

plt.plot(x_values, y_values_1, label=str(A))
plt.plot(x_values, y_values_2, label=str(B))

if largest_number <= 10:
    plt.xlim(0, 10)
    plt.ylim(0, 10)
elif largest_number <= 100:
    plt.xlim(0, 100)
    plt.ylim(0, 100) 
elif largest_number <= 1000:
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    
plt.xlabel("x")
plt.ylabel("y")
plt.fill_between(x_values, np.minimum(y_values_1, y_values_2), where=(y_values_1 >= 0) & (y_values_2 >= 0), alpha=.5)
plt.legend()
title1 = "Objective Function Value:", value(prob.objective)
title2 = "x =", value(x)
title3 ="y =", value(y)

plt.suptitle(title1+ title2+ title3)

plt.show()

