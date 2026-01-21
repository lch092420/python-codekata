# 백준 문제 10989
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/10989
# 작성자: 학생
# 작성일: 2026. 01. 21. 11:51:53

import sys
input = sys.stdin.readline

n = int(input())

count = [0] * 10001
for _ in range(n):
    count[int(input())] += 1
for i in range(len(count)):
    for _ in range(count[i]):
        print(i)