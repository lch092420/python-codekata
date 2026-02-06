# 약수의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 알고리즘: 수학, 반복문
# 작성자: 학생
# 작성일: 2026. 02. 06. 09:38:46

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer