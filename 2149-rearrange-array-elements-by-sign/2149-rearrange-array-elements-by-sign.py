class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        res = []
        for i in range(len(nums) // 2):
            res.append(positives[i])
            res.append(negatives[i])

        return res

        

