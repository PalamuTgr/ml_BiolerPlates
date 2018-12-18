from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = ‘red’)
plt.plot(X_train, regressor.predict(X_train),color = ‘blue’)
plt.title(‘Salary vs Experience(‘Training Set’)’)
plt.xlabel(‘Years of experience’)
plt.ylabel(‘Salary’)
plt.show()


plt.scatter(X_test, y_test, color = ‘red’)
plt.plot(X_train, regressor.predict(X_train),color = ‘blue’)
plt.title(‘Salary vs Experience(‘Test Set’)’)
plt.xlabel(‘Years of experience’)
plt.ylabel(‘Salary’)
plt.show()

