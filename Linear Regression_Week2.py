import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd
#
# table=pd.read_csv("Week2_LinearRegression_Table.csv")
# print(table)


m = 51
x = np.arange(1, m, 1)

y = 15 * x + 5 + np.random.normal(0.5, 10, x.shape)

# print(y)
#
plt.scatter(x,y)
plt.show()

w = np.random.randint(1, 100, 2)
w = np.array(w)
print(w)

err = 1
eps = 1.e-5
alph = 1.5
# J = [(0.5 / m) * np.sum((y - w[1] * x - w[0])**2)]

j_func = lambda w : (0.5 / m) * np.sum((y - w[1] * x - w[0])**2)
J = [j_func(w)]
J = np.array(J)
# print((J))

print('function starts')

error = []
error.append(err)

i = 0
while err > eps:
    yh = w[0] + w[1]*x
    w = [w[0] - (alph/m) * np.sum(yh - y),
         w[1] - (alph/m) * (np.sum(np.dot((yh - y), x)))]
    i += 1
    J = np.append(J, j_func(w))
    err = abs(J[i] - J[i-1])
    error.append(err)
    # print(err)

print(J[0] - J[1])
