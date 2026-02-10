# 나누어 떨어지는 숫자 배열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 알고리즘: 배열, 정렬
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:21:56

def solution(arr, divisor):
    a = []
    for i in arr:
        if i%divisor == 0 :
            a.append(i)
    if a==[]:
        a.append(-1)
    a.sort()
    return a