class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        answer = 0
        idx = 0

        for t in processorTime:
            longest_task = tasks[idx]
            answer = max(answer, t + longest_task)
            idx += 4
        return answer