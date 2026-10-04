from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for card in sorted(counts):
            count = counts[card]
            if count > 0:
                for i in range(groupSize):
                    if counts[card + i] < count:
                        return False
                    counts[card + i] -= count

        return True


        