limit = float(input())
n = int(input())
erk, pk, maxz, sm = 0, 0, float('-inf'), 0

#input обработка
for _ in range(n):
    try:
        pz = float(input())
    except:
        erk += 1
        continue
    if pz > limit:
        pk += 1
    maxz = max(maxz, pz)
    sm += pz

#output
print(n)
print(erk)
print(pk)
print(f'{maxz:.1f}')
print(f'{(sm/(n-erk)):.1f}')