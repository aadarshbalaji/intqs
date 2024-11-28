class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        time = 0
        start_to_index = {}
        end_to_index = defaultdict(list)
        index_to_chair = {}
        heap = []
        [heappush(heap,x) for x in range(len(times))]
        for i, friend in enumerate(times):
            start_to_index[friend[0]] = i
            end_to_index[friend[1]].append(i)
            
        for time in range(max(end_to_index.keys())):
            if time in end_to_index:
                for index in end_to_index[time]:
                    heappush(heap, index_to_chair[index])
            if time in start_to_index:
                index_to_chair[start_to_index[time]] = heappop(heap)

        return index_to_chair[targetFriend] 
        
        


