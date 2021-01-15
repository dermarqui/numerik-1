import numpy as np

def f(x,y):
  return 2*pow(x,4) - 3*pow(x,2)*y + pow(y,3)

#gewichte berechnen
def newtonCotes(n):
  A = np.zeros((n + 1, n + 1))
  v = np.zeros(n + 1)
  for i in range(n + 1):
    v[i] = 1 / (i + 1)
    for j in range(n + 1):
      A[i][j] = pow(j / n, i)
  
  w = np.linalg.solve(A, v)
  return w

#default: simpsonregel
def calcWeight(n):
  w = newtonCotes(n)
  #dyadisches produkt von w,w
  W = np.outer(w,w)
  return W

#4 integrationsgrenzen weil rechteck
#Gewichte mal funktionswerte im gitter aufaddieren
def integrate(xa,xb,ya,yb,f,n = 2):
  W = calcWeight(n) * (xb - xa) * (yb - ya)
  I = 0
  x = np.linspace(xa,xb,n+1)
  y = np.linspace(ya,yb,n+1)
  for i in range(n + 1):
    for j in range(n + 1):
      I += f(x[i],y[j])*W[i][j]

  return I

#Aufgabe a
print("a)")
Ia = integrate(0,9,0,9,f) - integrate(3,6,3,6,f)
print(Ia)

#Aufgabe b
print("b)")
Ib = 0
for i in range(1,4):
  for j in range(1,4):
    if ((i != 2) or (j != 2)):
      Ib += integrate(3*(i-1),3*i,3*(j-1),3*j,f)
print(Ib)

print("\nzum Vergleich: Der exakte Wert ist:")
print(190414.8)