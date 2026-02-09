# x만큼 간격이 있는 n개의 숫자
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 알고리즘: 배열
# 작성자: 학생
# 작성일: 2026. 02. 09. 09:20:40

def solution(x, n):
    answer = []
    p = x
    for i in range(n):
        answer.append(x)
        x+=p
    return answer