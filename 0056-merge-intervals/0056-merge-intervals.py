class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output=[]
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                output.append(curr)
                curr = intervals[i]
        output.append(curr)
        return output