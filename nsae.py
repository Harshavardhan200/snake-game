en = int(input("enter"))
f = en*2 - 1
n = []

for i in range(f):
    n.append([0 for j in range(f)])
print(n)
while f != 0:
    for i in range(f):
        for j in range(f):
            if i == 0 or i == f - 1 or j == 0 or j == f-1:
                n[i][j] = f
        f -= 1
print(n)