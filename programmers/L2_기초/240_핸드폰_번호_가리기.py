# 핸드폰 번호 가리기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:30:56

def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(phone_number)-4):
        answer[i] = '*'
    return ''.join(answer)