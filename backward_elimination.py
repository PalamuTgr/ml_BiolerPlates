dataset=pd.read_csv('Data.csv')
X=dataset.iloc[ : , :-1].values
y=dataset.iloc[:, 3].values


import statsmodels.formula.api as sm
# Add a column to dataset considering b0*x0 is 1
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis =1)
#Building the optimal model using BE
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit
regressor_OLS.summary()
#Remove predictor with highest p value.
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit
regressor_OLS.summary()
#Remove predictor with highest p value.
X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit
regressor_OLS.summary()
#y = b0*x0 + b1*x1 + b2*x2 + b3*x3 + … + bn*xn
