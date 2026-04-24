class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1

        arr = list(count.items())
        arr.sort(key=lambda p:p[1], reverse = True)

        ans = []
        for j in range(k):
            ans.append(arr[j][0])
        
        return ans

        