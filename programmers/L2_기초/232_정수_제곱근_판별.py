# 정수 제곱근 판별
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 알고리즘: 수학
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:14:15

def solution(n):
    rn = abs(n**(1/2))
    if abs(rn) % 1 == 0:
        return (rn+1)**2
    else:
        return -1