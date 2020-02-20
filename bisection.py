import math

# what need in e:
# func
# a0
# b0
# epsilon
# iteration
# specified


def printf(iter, a, b, p, fa, fp, err):
    print "{0}\t{1:.10f}\t{2:.10f}\t{3:.10f}\t{4:.10f}\t{5:.10f}\t{6:.10f}".format(iter, a, b, p, fa, fp, err)


def bisection(func, a, b, lp, epsilon, iter, max_iter=None):
    p = (a + b) / 2.0

    err = abs(p - lp)/abs(p)

    fa = func(a)
    fp = func(p)
    root = p

    printf(iter, a, b, p, fa, fp, err)

    if iter == max_iter:
        return (p, iter)

    if( err < epsilon ):
        return (p, iter)

    if( fa * fp > 0 ):
        newroot = bisection(func, p, b, p, epsilon, iter + 1, max_iter)
    else:
        newroot = bisection(func, a, p, p, epsilon, iter + 1, max_iter)

    return newroot


import e
root = 0
if e.specified == True:
    root = bisection(e.func, e.a0, e.b0, e.a0, e.epsilon, 1, e.iteration)
else:
    root = bisection(e.func, e.a0, e.b0, e.a0, e.epsilon, 1)
print root
