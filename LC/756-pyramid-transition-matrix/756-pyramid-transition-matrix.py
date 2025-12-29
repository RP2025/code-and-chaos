from collections import defaultdict
from functools import lru_cache
from itertools import pairwise, product
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for x in allowed:
            mp[x[:2]].append(x[2])

        @lru_cache(None)
        def dfs(s: str) -> bool:
            if len(s) == 1:
                return True

            rows = []
            for a, b in pairwise(s):
                if a + b not in mp:
                    return False
                rows.append(mp[a + b])

            return any(dfs("".join(p)) for p in product(*rows))

        return dfs(bottom)
