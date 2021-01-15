import numpy as np
import matplotlib.pyplot as mp

xtest = np.array([-1,-0.5,0,0.5,1])
ytest = np.array([10,7.1,5,3.6,2.5])

def interpolmatrix(x):
  n = (x.size - 1) / 2
  if (x.size%2) == 0:
    raise Exception("Gerade Anzahl an Stützstellen")

  A = np.zeros((x.size,x.size))

  for j in range(x.size):
    #ganze spalte
    A[:][j] = np.exp((j-n)*x[:])

  return A
   
def interpol(x,y):
  A = interpolmatrix(x.copy())
  a = np.linalg.solve(A,y)
  xVals = np.linspace(-1,1,100)
  yVals = np.zeros(100)
  n = (x.size - 1) / 2

  for j in range(x.size):
    yVals[:] += a[j] * np.exp((j-n)*xVals[:])

  mp.plot(xVals,yVals)
  mp.show()

interpol(xtest,ytest)

#testem mit anderen werten:
#interpol(np.array([-1,-0.5,0,0.5,1]), np.array([10,7.1,5,30.6,2.5]))