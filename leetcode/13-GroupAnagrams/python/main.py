class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = {}

        for str in strs:
            key = "".join(sorted(str))

            if not key in cache:
                cache[key] = []

            cache[key].append(str)

        return list(cache.values())
