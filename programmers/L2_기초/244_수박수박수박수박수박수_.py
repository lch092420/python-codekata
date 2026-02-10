# 수박수박수박수박수박수?
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:35:08

def solution(n):
    watermelon = []
    for i in range(n):
        if (i+1) % 2 ==1:
            watermelon.append('수')
        else:
            watermelon.append('박')
    return ''.join(watermelon)