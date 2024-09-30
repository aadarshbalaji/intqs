class Twitter(object):

    def __init__(self):
        self.people = defaultdict(set) #id to set of following
        self.tweets = [] #list of tweets

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.people[userId].add(userId)
        self.tweets.append([userId,tweetId])
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        arr = []
        for i in range(len(self.tweets)-1,-1,-1):
            if len(arr) >= 10:
                return arr
            user, tweet = self.tweets[i]
            if user in self.people[userId]:
                arr.append(tweet)
        return arr
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.people[followerId].add(followerId)
        self.people[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.people[followerId]:
            self.people[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)