limit = int(input())
n = int(input())
erk, pk, maxz, sm = 0, 0, 0, 0

for _ in range(n):
    pz = input()
    if isintance(str, pz):
        erk += 1
        continue
    else:
        pz = int(pz)
    if pz > limit:
        pk += 1
    maxz = max(maxz, pz)
    sm += pz