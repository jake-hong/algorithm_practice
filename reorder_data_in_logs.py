# 로그를 재정렬하라.
# 입력: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# 출력: logs = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6" ]

# 1.람다와 +연산자 이용

def reorderLogFiles(logs):
    letters, digits = [], []

    # 숫자와 문자를 판별
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))
