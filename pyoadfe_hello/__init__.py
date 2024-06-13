import numpy


def lstsq(A, b):
	return (np.linalg.inv(A.T @ A) @ A.T @ b)
