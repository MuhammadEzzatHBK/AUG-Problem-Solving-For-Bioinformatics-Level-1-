import matplotlib.pyplot as plt

seq = "TTGATTACCTTATTTGATCATTACACATTGTACGCTTGTGTCAAAATATCACATGTGCCT"
C = 0
G = 0
GCSkew = []

for ch in seq:
    if ch == 'C':
        C += 1
    elif ch == 'G':
        G += 1
    if G != 0 or C != 0:
        GCSkew.append((G-C)/(G+C))
    else:
        GCSkew.append(0)

plt.plot(range(len(seq)), GCSkew)
plt.show()
