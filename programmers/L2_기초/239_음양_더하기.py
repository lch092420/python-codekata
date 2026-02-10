# 음양 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 알고리즘: 배열
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:30:17

def solution(absolutes, signs):
    answer = 0
    c_signs = [x if x==1 else -1 for x in signs]
    for i in range(len(absolutes)):
        answer += absolutes[i]*c_signs[i]
    return answer