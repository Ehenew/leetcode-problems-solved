from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.freqCount = defaultdict(int)

    def add(self, number: int) -> None:
        self.freqCount[self.cnt[number]] -= 1
        self.cnt[number] += 1
        self.freqCount[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] > 0:
            self.freqCount[self.cnt[number]] -= 1
            self.cnt[number] -= 1
            self.freqCount[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)