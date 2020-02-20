import math

# what need in e:
# ode
# exact
# ddexact
# a0
# b0
# interval
# L (partial y)
# w0


def printf(iter, val, exact, err_bound, t, act_err):
    print "t = {4}, w{0} = {1:.10f}, exact = {2:.10f}, err_bound = {3:.10f}, act_err = {5:.10f}".format(iter, val, exact, err_bound, t, act_err)


def euler(func, exact, ddexact, a, b, interval, partial, w0):
    val = w0

    count = (b-a)/interval
    i = 0

    max_yt = abs(ddexact(a))
    if abs(ddexact(b)) > max_yt:
        max_yt = abs(ddexact(b))

    while i <= count:
        exa = exact(a + interval * i)
        act_err = abs(exa - val)
        err_bound = interval * max_yt * (math.pow(math.e, interval * i * partial) - 1.0) / 2.0 / partial
        printf(i, val, exa, err_bound, a+interval*i, act_err)

        val = val + interval * func(a + interval * i, val)

        i = i+1


import e

euler(e.ode, e.exact, e.ddexact, e.a0, e.b0, e.interval, e.L, e.w0)
