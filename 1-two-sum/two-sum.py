class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}  # 値 : インデックス

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in prev_map:
                # ここでreturnします（インデントに注意）
                return [prev_map[diff], i]
            
            prev_map[n] = i
        
        return []