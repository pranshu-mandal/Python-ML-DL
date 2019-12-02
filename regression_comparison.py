import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

table=pd.read_csv("Week2_LinearRegression_Table.csv")
print(table)

x = table['Temperature']
y = table['Thermal Coefficient']

print(x)
print(y)

plt.figure(figsize=(16,8))
plt.plot(x,y, 'o-')
plt.xlabel('Temperature')
plt.ylabel('Thermal Coefficient')
plt.vlines(70, np.min(y), np.max(y), label='70 $^o$C')
plt.legend()
plt.show()

