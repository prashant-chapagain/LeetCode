from collections import defaultdict


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        setArr2 = set(arr2)
        end = []
        result = []
        count = defaultdict(int)
        for num in arr1:
            if num not in setArr2:
                end.append(num)
            count[num] += 1
        end.sort()
        for n in arr2:
            for _ in range(count[n]):
                result.append(n)
        return result + end
        