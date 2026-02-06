# 자릿수 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 알고리즘: 문자열, 반복문
# 작성자: 학생
# 작성일: 2026. 02. 06. 09:26:43

def solution(n):
    s = 0
    while n >= 10:
        x = n % 10
        s += x
        n //= 10
    s += n
    return s