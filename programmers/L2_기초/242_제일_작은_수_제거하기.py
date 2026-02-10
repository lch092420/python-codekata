# 제일 작은 수 제거하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 알고리즘: 배열
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:34:53

def solution(arr):
    m = min(arr)
    if len(arr) != 1:
        answer = [x for x in arr if x != m]
    else:
        return [-1]
    return answer