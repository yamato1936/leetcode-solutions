class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                candidate_word = s[start:end]

                if dp[start] and candidate_word in word_set:
                    dp[end] = True
                    break
        
        return dp[n]
        