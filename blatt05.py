import numpy as np
import matplotlib.pyplot as mp

#Test-Daten aus der Aufgabe
xVals = np.empty(11)
yVals = np.empty(11)
for i in range(11):
  xVals[i] = i - 5
  yVals[i] = 1/(1+pow(xVals[i],2))

#Ergebnis der divDiff
divDiffList = np.empty(11)

#rekursiv die divDiffLit modifizieren/berechnen:
def divDiff(x,y,i,j):
  if j == 0 & i == 0:
    divDiffList[0] = y[0]
  if j == 0:
    return y[i]
  else:
    next = (divDiff(x,y,i+1,j-1) - divDiff(x,y,i,j-1)) / (x[i+j] - x[i])
    if i == 0:
      divDiffList[j] = next
    return next


#Funtion auswerten und printen
def hornerSchema(x,y):
  #div. diff. berechnen
  divDiff(x,y,0,x.size - 1)
  xValues = np.linspace(-5,5,500)
  yValues = np.ones(500)
  #Wahre Funktion
  f = 1/(1+pow(xValues[:],2))

  #Horner Schema zum auswerten anwenden
  yValues[:] = divDiffList[x.size-1]
  for i in range(x.size-2,-1,-1):
    yValues[:] = yValues[:] * (xValues[:] - x[i]) + divDiffList[i]

  #Plotten:
  mp.plot(xValues,yValues)
  mp.plot(xValues,f)
  mp.show()



#divDiff ausführen
divDiff(xVals,yVals,0,xVals.size-1)
print(divDiffList)

#interpol plotten
hornerSchema(xVals,yVals)