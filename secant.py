import math

# what need in e:
# func
# p0
# p1
# epsilon
# iteration
# specified

def printf(iter, llp, lp, p, diff):
    print "{0}\t{1:.10f}\t{2:.10f}\t{3:.10f}\t{4:.10f}".format(iter, llp, lp, p, diff)

def secant(func, llp, lp, epsilon, iter, max_iter=None):
    q0 = func(llp)
    q1 = func(lp)
    np = lp - q1 * (lp-llp)/(q1-q0)
    diff = abs(np-lp)

    printf(iter, llp, lp, np, diff)

    if diff < epsilon:
        return (np, iter)
    if iter == max_iter:
        return (np, iter)

    return secant(func, lp, np, epsilon, iter + 1, max_iter)


import e
if e.specified:
    root = secant(e.func, e.p0, e.p1, e.epsilon, 2, e.iteration)
else:
    root = secant(e.func, e.p0, e.p1, e.epsilon, 2)

print root
