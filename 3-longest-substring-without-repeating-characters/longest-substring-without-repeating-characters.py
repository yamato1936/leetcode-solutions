class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last: dict[str, int] = {}
        left = 0
        answer = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            
            last[ch] = right
            answer = max(answer, right - left + 1)

        return answer