class Twitter:

    def __init__(self):
        self.tweet_count = 0
        self.followers_map = defaultdict(set) # follower_id -> set(follwee_id_1,follwee_id_2,follwee_id_3)
        self.post_map = defaultdict(list) # user_id -> list([tweet_count,tweet_id])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_map[userId].append([self.tweet_count,tweetId])
        # for using in max heap
        self.tweet_count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        # a user can follow themself
        self.followers_map[userId].add(userId)
        # get the list of followeeId the user follows
        for followeeId in self.followers_map[userId]:
            # for each followeeId get the list of recent tweets
            if followeeId in self.post_map:
                # get the recent tweet index for the foloweeId tweetes 
                recent_tweet_index = len(self.post_map[followeeId]) - 1
                # latest tweet by followeeId
                tweet_count,tweet_id = self.post_map[followeeId][recent_tweet_index]
                # add the tweet into heap to process further
                max_heap.append([tweet_count,tweet_id,followeeId,recent_tweet_index-1])
        # heapify the max_heap
        heapq.heapify(max_heap)
        
        while max_heap and len(res) < 10:
            # most recent tweet among all the followers
            tweet_count,tweet_id,followeeId,index = heapq.heappop(max_heap)
            # add the most recent tweet into result
            res.append(tweet_id)
            # get the other prev tweet for the followeeId and prev index
            if(index >= 0):
                tweet_count,tweet_id = self.post_map[followeeId][index]
                # for the current followeeId add the other tweets into heap
                heapq.heappush(max_heap,[tweet_count,tweet_id,followeeId,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followeeId into for the followerId
        self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId if user follow the followee
        if followeeId in self.followers_map[followerId]:
            self.followers_map[followerId].remove(followeeId)
            
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)