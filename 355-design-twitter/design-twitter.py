class Twitter(object):

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set) # x: [y,z], x is following y and z
        self.tweets = defaultdict(list)


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        self.tweets[userId].append([self.time, tweetId])
        
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        target_tweeters = list(self.following[userId]) + [userId]

        for user in target_tweeters:
            for timestamp, tweet in self.tweets[user][-10:]:
                heappush(heap, [-timestamp, tweet])
        
        rv = []
        while heap and len(rv) < 10:
            rv.append(heappop(heap)[1])
        return rv
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)