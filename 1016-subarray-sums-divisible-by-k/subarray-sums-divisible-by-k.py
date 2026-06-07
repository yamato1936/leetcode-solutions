from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums:List[int], k:int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        current_sum = 0
        answer = 0

        for i in nums:
            current_sum += i
            
            remainder = current_sum % k

            answer += prefix_count[remainder]
            
            prefix_count[remainder] += 1

        return answer