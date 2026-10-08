def winner(names: list[str], scores: list[float]) -> str:
    res: str = ''
    maxv: int = 0
    for n, s in zip(names, scores):
        if s > maxv:
            res = n
            maxv = s
    return res

def average(scores: list[float]) -> float:
    return float(f'{sum(scores)/len(scores):.2f}') if scores else 0.0

#def ranking(names: list[str], scores: list[float]) -> list[str]:

#def above_average(names: list[str], scores: list[float]) -> list[str]:



names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,  9.0]

print(winner(names, scores))
print(average(scores))