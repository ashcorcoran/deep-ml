import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)

	X_trans = X.T
	beta = np.linalg.inv(X_trans @ X) @ X_trans @ y
	theta = np.round(beta, 4).tolist()
	return theta