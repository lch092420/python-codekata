# 내적
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 알고리즘: 배열, 수학
# 작성자: 학생
# 작성일: 2026. 03. 12. 23:03:30

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer