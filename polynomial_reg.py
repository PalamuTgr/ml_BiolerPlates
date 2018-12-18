
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)



from sklearn.preprocessing import PolynomialFeatures
polyReg = PolynomialFeatures (degree =2)
X_poly = poly_reg.fit_transform(X)

L_in_reg2 = LinearRegression()
Lin_reg2.fit(X_poly, y)



y_pred = lin_reg.predict(X_test)
plt.scatter(X, y, color = ‘red’)
plt.plot(X, lin_reg.predict(X),color = ‘blue’)
plt.title(‘Salary vs Experience(‘Linear Regression’)’)
plt.xlabel(‘Years of experience’)
plt.ylabel(‘Salary’)
plt.show()




y_pred = lin_reg2.predict(X_test)
plt.scatter(X_train, y_train, color = ‘red’)
plt.plot(X_train, lin_reg.predict(poly_reg.fit_transform(X)),color = ‘blue’)
plt.title(‘Salary vs Experience(‘Polynomial Regression’)’)
plt.xlabel(‘Years of experience’)
plt.ylabel(‘Salary’)
plt.show()
