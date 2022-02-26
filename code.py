# Libraries
import random
import matplotlib


# Constants
import matplotlib.pyplot as plt

Samples_X = []
Samples_Y = []
Classifications = []
ClassificationsWithRandomChange = []
d = 2
N = 100
a = random.uniform(-10, 10)
b = random.uniform(-10, 10)
# Y = a*X + b


# Random Line Function
def randomLineFunction(X):
    return a*X+b


# Make the random spots
for i in range(0, 100):
    Samples_X.append(random.uniform(-20, 20))
    Samples_Y.append(random.uniform(-20, 20))


# Primary Classification
for i in range(0, 100):
    Class = randomLineFunction(Samples_X[i])
    if Class >= Samples_Y[i]:
        Classifications.append(1)
    else:
        Classifications.append(0)


# Randomly change the class
ClassificationsWithRandomChange = Classifications
for i in range(0, 100):
    if random.randint(1, 10) == 10:
        if ClassificationsWithRandomChange[i] == 0:
            ClassificationsWithRandomChange[i] = 1
        else:
            ClassificationsWithRandomChange[i] = 0


print(a, b, randomLineFunction(499))
print("------------------------------------")
print(Samples_X)
print("------------------------------------")
print(Samples_Y)
print("------------------------------------")
print(Classifications)
print("------------------------------------")
print(ClassificationsWithRandomChange)


# Plots
# plt.scatter(Samples_X,Samples_Y,c=Classifications)
# plt.show()
plt.scatter(Samples_X, Samples_Y, c=ClassificationsWithRandomChange)
plt.show()
