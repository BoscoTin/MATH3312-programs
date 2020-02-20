# just change this m and then run to get the steps
m = [
    [1.0, 1.0, 0.0, 3.0, 1.0],
    [2.0, 1.0, -1.0, 1.0, 0.0],
    [3.0, -1.0, -1.0, 2.0, 3.0],
    [-1.0, 2.0, 3.0, -1.0, 2.0]
]




def column(m, c):
  return [m[i][c] for i in range(len(m))]

def row(m, r):
  return m[r][:]

def height(m):
  return len(m)

def width(m):
  return len(m[0])

def print_matrix(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

def gaussian_elimination_with_pivot(m):
  # forward elimination
  n = height(m)
  for i in range(n):
    pivot(m, n, i)
    for j in range(i+1, n):
      m[j] = [m[j][k] - m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]
      print "Perform substitution: row {} by row {}".format(j+1,i+1)
      print_matrix(m)

  if m[n-1][n-1] == 0: raise ValueError('No unique solution')

  # backward substitution
  x = [0] * n
  for i in range(n-1, -1, -1):
    s = sum(m[i][j] * x[j] for j in range(i, n))
    x[i] = (m[i][n] - s) / m[i][i]
  return x

def pivot(m, n, i):
  max = -1e100
  for r in range(i, n):
    if max < abs(m[r][i]):
      max_row = r
      max = abs(m[r][i])
  m[i], m[max_row] = m[max_row], m[i]
  if i != max_row:
      print "Swapping row {} and {}".format(i + 1, max_row + 1)
      print_matrix(m)



print(gaussian_elimination_with_pivot(m))
