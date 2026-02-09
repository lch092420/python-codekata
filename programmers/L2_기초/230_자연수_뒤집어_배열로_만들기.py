# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 학생
# 작성일: 2026. 02. 09. 09:21:56

def solution(n):
    answer=[]
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer