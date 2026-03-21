import markowitz_cpp
def markowitz(Sigma, wb, w_prev, lambda_turnover):
    w_opt = markowitz_cpp.optimize_portfolio(Sigma, wb, w_prev, lambda_turnover)
    return w_opt
