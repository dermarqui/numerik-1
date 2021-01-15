import numpy as np
import matplotlib.pyplot as mp

#funktionen definieren:
def functiona(x):
  return x*np.sin(np.pi*(x + 1))
  
def euler(x):
  return pow(np.e, 2 * pow(x, 2))

def newtonCotes(n,a,b,f):
  #Vandermonde matrix
  A = np.zeros((n + 1, n + 1))

  v = np.zeros(n + 1)
  y = np.zeros(n + 1)
  for i in range(n + 1):
    y[i] = f(i * (b - a) / n + a)
    v[i] = 1 / (i + 1)
    for j in range(n + 1):
      A[i][j] = pow(j / n, i)

  #gewichte berechnen durch lösen des lgs
  w = np.linalg.solve(A, v)

  integral = np.sum(w[:] * y[:]) * (b-a)
  return integral

#gewichte für die zusmmengesetzten newton cotes berechnen
def newtonCotesForComposite(n,a,b,f):
  A = np.zeros((n + 1, n + 1))
  v = np.zeros(n + 1)
  for i in range(n + 1):
    v[i] = 1 / (i + 1)
    for j in range(n + 1):
      A[i][j] = pow(j / n, i)
  
  w = np.linalg.solve(A, v)
  return w

def compositeNewtonCotes(n,a,b,N,f):
  y = np.zeros(N * (n + 1))
  H = (b - a) / N
  for i in range(y.size):
    y[i] = f(a + i * H / n)
  integral = 0

  for j in range(N):
    integral += newtonCotesForComposite(n,a + H * j, a + H * (j + 1),f)[:] * y[(j*n):((j+1)*n+1)]*H

  return np.sum(integral)


#ausgeben der aufgabe a
print("a)")
for i in range(1,5):
  s = "newton Cotes für n = " + str(i)
  print(s)
  print(newtonCotes(i,-1,2,functiona))

#aufgabe b plotten (x-Achse: N)
print("b) im plot")
X = range(1,11)
Y = np.zeros(10)
Y2 = np.zeros(10)
for i in range(1,11):
  #n=1
  Y[i-1] = (compositeNewtonCotes(1,1,2,i,euler))
for i in range(1,11):
  #n=2
  Y2[i-1] = (compositeNewtonCotes(2,1,2,i,euler))
mp.plot(X,Y,X,Y2)
mp.show()