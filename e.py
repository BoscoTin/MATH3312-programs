import math



func = lambda x: math.pow( math.e, -math.pow(x,2) )
dfunc = lambda x: -math.sin(x) - 1

#ddfunc = lambda x: -1/math.pow(x, 2)
ddfunc = lambda x: (1/x + 2/math.pow(x, 2) + 2/math.pow(x,3)) * math.pow(math.e, -x)
d4func = lambda x: (1/x + 4/math.pow(x, 2) + 12/math.pow(x,3) + 24/math.pow(x,4) + 24/math.pow(x,5)) * math.pow(math.e, -x)

# euler method
ode = lambda t,y: -y - math.pow(t, 2) * math.pow(y, 0.5)
exact = lambda t: math.pow(t+1, 2) - 0.5 * math.pow(math.e, t)
ddexact = lambda t: 2 - 0.5 * math.pow(math.e, t)
L = 1.0
w0 = 2



iteration = 3
specified = False
epsilon = math.pow(10, -10)


# step and interval and bound
a0 = 1
b0 = 2
interval = 0.1
# ends

# fixed and newton
p0 = 0.5
p1 = math.pi / 4
# fixed ends

# lagrange, dividediff, forwarddiff
xs = [0.1, 0.05, 0.01]
xv = 1.8
# lagrange, dividediff, forwarddiff ends
