import random
from typing import List

def reservoir_sample(rows: List[List[str]], k: int = 5, seed: int = 42) -> List[List[str]]:
    if len(rows) <= k: return list(rows)
    rng = random.Random(seed)
    res = list(rows[:k])
    for i in range(k, len(rows)):
        j = rng.randint(0, i)
        if j < k: res[j] = rows[i]
    return res
