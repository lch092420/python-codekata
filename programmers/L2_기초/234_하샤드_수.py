# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:16:54

def solution(x):
    s = sum(int(i) for i in str(x))
    return x%s == 0