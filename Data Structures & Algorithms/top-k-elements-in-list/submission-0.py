from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        sorted_items = sorted(freq.items(),
                              key=lambda x: x[1],
                              reverse=True)

        return [sorted_items[i][0] for i in range(k)]