class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
       
        inserted = False
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted = True
                break


        if not inserted:
                intervals.append(newInterval)

        ret_intervals = []
        for interval in intervals:
            if not ret_intervals or ret_intervals[-1][1] < interval[0]:
                ret_intervals.append(interval)
            else:
                ret_intervals[-1] = [ret_intervals[-1][0],max(ret_intervals[-1][1], interval[1])]
        return ret_intervals