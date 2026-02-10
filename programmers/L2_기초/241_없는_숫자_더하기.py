# 없는 숫자 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 알고리즘: 배열, 해시
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:33:52

def solution(numbers):
    answer = 0
    for i in range(10):
        if numbers.count(i) == 0:
            answer += i
    return answer