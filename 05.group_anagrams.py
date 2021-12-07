# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# input = ["eat","tea","tan","ate","nat","bat"]
# output=
#    [
#     ["ate","eat","tea"]
#     ["nat","tan"]
#     ["bat"]
#    ]

# 정렬하여 비교하기.

import collections


def groupAnagrams(string):
    anagrams = collections.defaultdict(list)

    for word in string:
        anagrams[''.join(sorted(word))].append(word)
        print(sorted(word))
    return anagrams.values()


string = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(string))
