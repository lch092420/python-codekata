# 콜라츠 추측
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 알고리즘: 시뮬레이션, 반복문
# 작성자: 학생
# 작성일: 2026. 02. 10. 09:21:16

def solution(num):
    cnt=0
    while cnt <500 and num !=1 :
        cnt += 1
        if (num & 1) == 0:
            num = num//2
        else:
            num = num*3+1
    return cnt if num==1 else -1