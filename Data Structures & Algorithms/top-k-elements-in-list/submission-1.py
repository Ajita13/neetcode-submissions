from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        arr = sorted(d.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(arr[i][0])

        return result


# Testing
solution = Solution()

nums = [1, 2, 2, 3, 3, 3]
k = 2

print(solution.topKFrequent(nums, k))