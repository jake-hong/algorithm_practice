
# 금지된 단어를 제외한 가장 흔히 등장하는 단어를 출력하라. 대소문자 구분을 하지 않고, 구두점도 무시한다.
# 입력: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# 출력 : "ball"

# 1.리스트 컴프리헨션, counter 객체 사용

# Data cleansing 필요

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def mostCommonWord(paragraph):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(mostCommonWord(paragraph))
