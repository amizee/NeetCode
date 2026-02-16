from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currSet, combinations = [], []
        self.helper(1, n, k, currSet, combinations)
        return combinations

    def helper(self, i, n, k, currSet, combinations):
        if len(currSet) == k:
            combinations.append(currSet.copy())
            return 
        elif i > n:
            return 
        
        currSet.append(i)
        self.helper(i + 1, n, k, currSet, combinations)
        currSet.pop()
        self.helper(i + 1, n, k, currSet, combinations)

# Intuition: similar to subsets but different base case where you stop at a subset of size k and in the case that a combination is never found with at least k values (empty subset) we return too.

# Time: O(k * C(n, k))
def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return

    for j in range(i, n + 1):
        curComb.append(j)
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop()
  
# Intuition: slightly more optimal where you can think about it like combinatorics in math.
# For example if n=5 and k=2, the first value can be 1-5 and the second value can be any of the 4 other numbers.
# Effectively the decision tree is now height k and at each decision there are 4 options.
# To prevent duplicates we only consider numbers higher than the current number we're looking at because this lower numbers have been considered already.
