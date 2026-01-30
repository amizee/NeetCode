import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # userID: set
        self.tweets = defaultdict(list) # userID: list of [count, tweetId] pairs
        self.n = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.n, tweetId])
        self.n += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            if self.tweets[followee]:
                count, tweetId = self.tweets[followee][-1]
                heapq.heappush(maxHeap, [-count, tweetId, followee, len(self.tweets[followee]) - 1])

        res = []
        while maxHeap:
            if len(res) == 10:
                break

            tweet = heapq.heappop(maxHeap)
            count, tweetId, uid, index = tweet[0], tweet[1], tweet[2], tweet[3]
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweets[uid][index - 1]
                heapq.heappush(maxHeap, [-count, tweetId, uid, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

# Intuition: track the followers mapping uid to a set and tweets mapping a uid to a list.
# To get the news feed, store the most recent tweet from each follower in a max heap. Then, add the next most recent for this same follower back to the heap by storing the index as well.
# This avoids having to go through every tweet and reduces the space complexity