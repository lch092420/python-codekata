# 약수의 개수와 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 알고리즘: 수학
# 작성자: 학생
# 작성일: 2026. 03. 12. 23:24:49

def solution(left, right):
    total = 0
    for i in range(left, right + 1):
        cnt = 0
        for x in range(1, i + 1):
            if i % x == 0:
                cnt += 1
        if cnt % 2 == 0:
            total += i
        else:
            total -= i
    return total