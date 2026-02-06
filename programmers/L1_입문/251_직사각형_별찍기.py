# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 학생
# 작성일: 2026. 02. 06. 09:20:50

n, m = map(int, input().strip().split(' '))
def rectangle(x,y):
    for _ in range(y):
        print('*'* x)  
rectangle(n,m)