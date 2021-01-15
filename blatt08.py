import numpy as np
import scipy.linalg as sp


#A aus R^mxn mit m>=n, Array mit Zielwerten f aus R^m
#@ ist das Malzeichen für Matrixmultiplikation (ersetzt matmul)
def Ausgleich(A, f):
    n = np.size(A, 1)

    #QR-Zerlegung von A
    Q, R = np.linalg.qr(A)
    c = np.transpose(Q) @ f
    c1 = c[0:n]
    R1 = R[0:n]
    x_QR1 = np.linalg.solve(R1, c1)

    #QR-Zerlegung von AtA
    Q, R = np.linalg.qr(np.transpose(A) @ A)
    y = np.transpose(A) @ f
    x_QR2 = np.linalg.solve(R, np.transpose(Q) @ y)

    #LR_Zerlegung von AtA
    P, L, R = sp.lu(np.transpose(A) @ A)  #P ist permutationsmatrix
    y = np.transpose(A) @ f
    x_LR = np.linalg.solve(R, np.linalg.solve(L, P.transpose() @ y))

    return [x_QR1, x_QR2, x_LR]


#Test (Bsp.: 5.4):
A = np.array([[1.0, 0], [1, 1], [1, 2], [1, 3]])
f = np.array([0, 10, 10, 20])
print("Berechnen des Bsp. 5.4:")
print(Ausgleich(A, f))
print("Referenz: [1, 6]")

#b _______________________________________-


def calcA(xsi, n):
    A = np.zeros((np.size(xsi), n))
    for i in range(np.size(xsi)):
        for j in range(n):
            A[i][j] = pow(xsi[i], j)
    return A


nlist = np.array([5, 11, 16, 21, 26])
coeff = np.array([0, 0, 1])
print("n \t eps \t\t qr1 \t\t\t\t\t\t qr2 \t\t\t\t\t\t lr")

#ns
for n in nlist:
    while np.size(coeff) < (n + 1):
      #0 an coeff dranhängen
        coeff = np.append(coeff, 0)
    #epsilons
    for k in range(2, 5):
        x = np.array([])
        f = np.array([])
        eps = 1 / (k * (n - 1))
        #xi s durch
        for i in range(n):
            x = np.append(x, i / n)
            x = np.append(x, i / n + eps)
        x = np.append(x, 1)
        for el in x:
            f = np.append(f, pow(el, 2))
        A = calcA(x, n + 1)
        #Ausgleichsproblem
        x_QR1, x_QR2, x_LR = Ausgleich(A, f)
        #Abweichungen berechnen
        norm1 = np.linalg.norm(x_QR1 - coeff)
        norm2 = np.linalg.norm(x_QR2 - coeff)
        norm3 = np.linalg.norm(x_LR - coeff)
        #Abweichungen ausgeben
        s = str(n) + "\t"
        s += str(round(eps, 5)) + "\t\t"
        s += str(norm1) + "\t\t"
        s += str(norm2) + "\t\t"
        s += str(norm3) + "\t\t"
        print(s)

#print(x)
