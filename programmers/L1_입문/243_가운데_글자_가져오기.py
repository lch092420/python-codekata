# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 02. 06. 09:11:50

def solution(s):
    r = len(s)
    return s[r//2] if r%2==1 else s[r//2-1:r//2+1]