def winner(names: list[str], scores: list[float]) -> str:
    res: str = ''
    maxv: float = float("-inf")
    for n, s in zip(names, scores):
        if s > maxv:
            res = n
            maxv = s
    return res

def average(scores: list[float]) -> float:
    return float(f'{sum(scores)/len(scores):.2f}') if scores else 0.0

def ranking(names: list[str], scores: list[float]) -> list[str]:
    si = sorted(range(len(scores)), key=lambda i: -scores[i])
    
    return [names[i] for i in si]    

def above_average(names: list[str], scores: list[float]) -> list[str]:
    av = average(scores)
    return [x for x, y in zip(names, scores) if y > av]
