import math

# what need in e:
# func
# dfunc
# p0
# epsilon
# iteration
# specified


def printf(iter, lp, flp, dflp, np, diff):
    print "{0}\t{1:.10f}\t{2:.10f}\t{3:.10f}\t{4:.10f}\t{5:.10f}".format(iter, lp, flp, dflp, np, diff)

def newton(func, dfunc, lp, epsilon, iter, max_iter=None):
    flp = func(lp)
    dflp = dfunc(lp)
    np = lp - flp/dflp
    diff = abs(np-lp)

    printf(iter, lp, flp, dflp, np, diff)

    if diff < epsilon:
        return (np, iter)
    if iter == max_iter:
        return (np, iter)

    return newton(func, dfunc, np, epsilon, iter + 1, max_iter)


import e
if e.specified:
    root = newton(e.func, e.dfunc, e.p0, e.epsilon, 1, e.iteration)
else:
    root = newton(e.func, e.dfunc, e.p0, e.epsilon, 1)

print root
