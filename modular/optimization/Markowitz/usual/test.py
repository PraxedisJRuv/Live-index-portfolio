import numpy as np
import markowitz_cpp

n = 5

Sigma = np.random.rand(n,n)
Sigma = Sigma @ Sigma.T
Sigma = Sigma.astype(np.float64)

wb = np.array([0.1,0.03,0.7,0.07,0.1], dtype=np.float64)
print(sum(wb))
# señal de alpha (ejemplo)
alpha = np.random.randn(n).astype(np.float64)

lambda_ = 0.1

w = markowitz_cpp.optimize_portfolio(Sigma, wb, alpha, lambda_)
print(w)