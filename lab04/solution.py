def winner(names: list[str], scores: list[float]) -> str:
    res: str = ''
    maxv: float = 0
    for n, s in zip(names, scores):
        if s > maxv:
            res = n
            maxv = s
    return res

def average(scores: list[float]) -> float:
    return float(f'{sum(scores)/len(scores):.2f}') if scores else 0.0

def ranking(names: list[str], scores: list[float]) -> list[str]:
    res = {}
    for x, y in zip(names, scores):
        res[x] = y
    print(sorted(res, reverse=True))

def above_average(names: list[str], scores: list[float]) -> list[str]:
    return [x for x, y in zip(names, scores) if y > av]



names =  ["Аня", "Боря", "Вика"]
scores = [7.0, 9.0,  9.0]

wnr = winner(names, scores)
av = average(scores)
above_av = above_average(names, scores)
print(ranking(names, scores))