class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        currlist = self.hashmap[key]
        left, right = 0, len(currlist) - 1
        while left <= right:
            mid = (left + right) // 2
            if currlist[mid][0] == timestamp:
                return currlist[mid][1]
            elif currlist[mid][0] < timestamp:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        if right >= 0:
            return currlist[right][1]
        
        return ""
    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)