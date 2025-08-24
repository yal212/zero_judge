# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         start = intervals[0]
#         end = intervals[1]
#         i = 1
#         ans = []
#         while start != end:
#             if start[1] >= end[0]:
#                 ans.append([start[0], end[1]])
#                 i += 1
#             else:
#                 ans.append(start)
#                 ans.append(end)
#             if i+2 <= len(intervals):
#                 start = intervals[i]
#                 i += 1
#                 end = intervals[i]
#             elif i < len(intervals):
#                 start = intervals[i]
#         return ans

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        def l(x):
            return x[0]

        intervals.sort(key=l)
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]
            if current[0] <= prev[1]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged
