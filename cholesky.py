import numpy as np

#Test-Array erzeugen. 16.0 wird als double aufgefasst
A = np.array([[16.0, 4, 4, 0], [4, 5, 1, 2], [4, 1, 2, -1], [0, 2, -1, 6]])


#Methode, die den Cholesky Faktor zur gegebenen Matrix zurückgibt
def cholesky(matrix):
    #Dim. der Matrix entspricht der Größe der ersten Zeile der Matrix, da die Matrix quadratisch ist n.V.
    n = matrix[0].size
    #erzeuge leere Matrix mit genau den gleichen Dimensionen wie die Eingabematrix
    L = np.zeros_like(matrix)
    #setze den ersten Wert nach der Choleskyzerl.
    L[0][0] = np.sqrt(matrix[0][0])
    #setze iterativ die weiteren Werte nach der Choleskyzerl.
    for i in range(1,n):
        for j in range(0, i):
            sum = np.sum(L[i] * L[j])
            L[i][j] = (matrix[i][j] - sum)/L[j][j]
        L[i][i] = np.sqrt(matrix[i][i] - np.sum(pow(L[i],2)))
    
    #gebe den Choleskyfaktor L zurück
    return L

#Ausführen des Programms
print("Die Matrix A = ")
print(A)
print("\nDer Cholesky Faktor L = ")
L = cholesky(A)
print(L)
#testen des Programs:
print("\nL*L(transponiert) ist:")
print(np.matmul(L,L.transpose()))
print("\nDer Cholesky Faktor nach numpy ist:")
print(np.linalg.cholesky(A))