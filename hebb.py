# Guilherme Alves

"""
    Trainamento de um neurônio 

"""

# Inputs
x1 = [-1, 1, -1, 1]
x2 = [-1, -1, 1, 1]

# Output
t = [-1, -1, -1, 1]

# Deltas
w1v = []
w2v = []
bv = []

k = 0
for i in x1:
    w1v.append(i*t[k])
    k = k + 1

k = 0
for i in x2:
    w2v.append(i * t[k])
    k = k + 1

# Pesos
w1 = []
w2 = []
b = []

w1.append(w1v[0])
w2.append(w2v[0])
b.append(t[0])

# Calculando os pesos
k = 0
while k != 3:
    w1.append(w1v[k+1] + w1[k])
    w2.append(w2v[k+1] + w2[k])
    b.append(b[k] + t[k+1])
    k = k+1

# Printando os pesos após o treinamento
print(w1[3])
print(w2[3])
print(b[3])