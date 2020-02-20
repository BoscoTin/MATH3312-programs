import numpy as np

# change A and B, no need anything in e
A = [
    [1,1,0,3],
    [2,1,-1,1],
    [3,-1,-1,2],
    [-1,2,3,-1]
]

B = [8,7,14,-7]

a = np.array(A)
b = np.array(B)


def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def linearsolver(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass
     print "swap row {}, {}".format(k + 1, i + 1)
     pprint(M)


   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]

       print "minus row {} by {} times row {}".format(j + 1, q, k + 1)
       pprint(M)


  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  print x



linearsolver(A,B)
x = np.linalg.solve(a, b)
print x
