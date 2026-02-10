# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:17:35

def solution(a, b):
    s = 0
    if a <= b:
        for i in range(a,b+1):
            s+=i
    else:
        for i in range(b,a+1):
            s+=i
    return s