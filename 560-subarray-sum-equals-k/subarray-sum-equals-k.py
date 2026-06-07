from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k:int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        answer = 0

        for i in nums:
            current_sum += i

            need = current_sum - k
            answer += prefix_count[need]

            prefix_count[current_sum] += 1

        return answer