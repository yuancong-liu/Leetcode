# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Andy = {list1[i]: i+1 for i in range(len(list1))}

        Doris = {list2[i]: i+1 for i in range(len(list2))}

        diff = list(set(list1).union(set(list2)) - set(list1).intersection(set(list2)))

        Andy = Counter(Andy)
        Doris = Counter(Doris)
        indexSum = Andy + Doris
        for restaurant in diff:
            if restaurant in diff:
                del indexSum[restaurant]

        minIndexSum = min(indexSum.values())
        result = [item for item in indexSum.keys() if indexSum[item] == minIndexSum]

        return result

# leetcode submit region end(Prohibit modification and deletion)
