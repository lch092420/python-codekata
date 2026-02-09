# 나머지가 1이 되는 수 찾기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 알고리즘: 수학, 반복문
# 작성자: 학생
# 작성일: 2026. 02. 09. 09:19:57

def solution(n):
    x=1
    while n%x!=1:
        x+=1
    answer = x
    return answer