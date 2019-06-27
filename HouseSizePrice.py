import matplotlib.pyplot as plt
import numpy as np 

from sklearn import datasets, linear_model 

housePrice = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
houseSize = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

plt.scatter(houseSize,housePrice, color='red')

plt.ylabel('House Price')
plt.xlabel('House Size')

plt.show()

houseSizetraining = np.array(houseSize).reshape((-1,1))

#Fitting into the model

regression = linear_model.LinearRegression()

regression.fit(houseSizetraining, housePrice)

print('Coefficients: \n',regression.coef_)
print('intercept: \n', regression.intercept_)

def graph(formula, x_range):
		x = np.array(x_range)
		y = eval(formula)
		plt.plot(x,y)

#plotting the prediction line 

graph('regression.coef_*x+regression.intercept_',range(1000,2700))
print(regression.score(houseSizetraining, housePrice))

plt.scatter(houseSize,housePrice,color='red')
plt.ylabel('House Price')
plt.xlabel('Size of the house')
plt.show()
