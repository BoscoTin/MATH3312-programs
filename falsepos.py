import math

# what need in e:
# func
# p0
# p1
# epsilon
# iteration
# specified (to perform max_iter)

def printf(iter, llp, lp, p, diff):
    print "{0}\t{1:.10f}\t{2:.10f}\t{3:.10f}\t{4:.10f}".format(iter, llp, lp, p, diff)

def falsepos(func, llq, lq, llp, lp, epsilon, iter, max_iter=None):
    np = lp - lq * (lp-llp)/(lq-llq)
    nq = func(np)
    diff = abs(np-lp)

    printf(iter, llp, lp, np, diff)

    if diff < epsilon:
        return (np, iter)
    if iter == max_iter:
        return (np, iter)


    if (nq*lq < 0):
        return falsepos(func, lq, nq, lp, np, epsilon, iter + 1, max_iter)
    else:
        return falsepos(func, llq, nq, llp, np, epsilon, iter + 1, max_iter)

import e
if e.specified:
    root = falsepos(e.func, e.func(e.p0), e.func(e.p1), e.p0, e.p1, e.epsilon, 2, e.iteration)
else:
    root = falsepos(e.func, e.func(e.p0), e.func(e.p1), e.p0, e.p1, e.epsilon, 2)

print root
