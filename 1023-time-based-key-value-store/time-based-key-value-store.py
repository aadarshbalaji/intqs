class TimeMap(object):

    def __init__(self):
        self.word_to_times = defaultdict(list)
        self.word_to_time_to_val = defaultdict(dict)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.word_to_times[key].append(timestamp)
        self.word_to_time_to_val[key][timestamp] = value

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.word_to_times or self.word_to_times[key][0] > timestamp:
            return ''
        arr = self.word_to_times[key]
        l = 0 
        r = len(arr)-1
        fin = l
        while l <= r:
            mid = (l + r) //2
            if arr[mid] == timestamp:
                fin = mid
                break
            if arr[mid] > timestamp:
                r = mid - 1
            else:
                fin = mid
                l = mid + 1
        return self.word_to_time_to_val[key][arr[fin]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)