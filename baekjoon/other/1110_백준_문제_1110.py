# 백준 문제 1110
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/1110
# 작성자: 학생
# 작성일: 2026. 01. 20. 11:15:28

import sys
input = sys.stdin.readline

n = int(input())

def solve(n):
    cnt = 1
    x = n // 10
    y = n % 10
    a = (x + y) % 10
    b = y * 10 + a
    while n != b:
        x = b // 10
        y = b % 10
        a = (x+y)%10
        b = y*10 + a
        cnt+=1
    print(cnt)
solve(n)