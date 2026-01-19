# 백준 문제 2869
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/2869
# 작성자: 학생
# 작성일: 2026. 01. 19. 17:23:36

import sys 
input = sys.stdin.readline
a,b,v = map(int,input().split())

def solution(x, y, z):
    return (z - x + (x - y) - 1) // (x - y) + 1


print(solution(a,b,v))
