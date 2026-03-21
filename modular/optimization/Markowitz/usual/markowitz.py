import markowitz_cpp
def markowitz(Sigma, wb):
    w = markowitz_cpp.optimize_portfolio(Sigma, wb)
    return w