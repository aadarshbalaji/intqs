class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        curr_cooked = timeSeries[0] + duration - 1
        total_cooked = duration 
        for t in timeSeries[1:]:
            bigtime = t + duration - 1
            if t <= curr_cooked:
                offset = bigtime - curr_cooked 
                total_cooked += offset
                curr_cooked += offset
            else:
                curr_cooked = bigtime
                total_cooked += duration

        return total_cooked
