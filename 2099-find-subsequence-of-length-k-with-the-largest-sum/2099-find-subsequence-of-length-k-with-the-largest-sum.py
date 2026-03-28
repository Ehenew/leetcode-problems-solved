class Solution:
    def maxSubsequence(self, nums, k):
        pairs = [(num, i) for i, num in enumerate(nums)]
        
        pairs.sort(key=lambda x: x[0], reverse=True)
        top_k = pairs[:k]
        
        top_k.sort(key=lambda x: x[1])
        
        return [num for num, _ in top_k]