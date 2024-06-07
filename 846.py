class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range (first,first+groupSize):
                if i not in count:
                    return False
                count[i] -=1
                if(count[i]==0):
                    if (i != minHeap[0]):
                        return False
                    heapq.heappop(minHeap)
        return True