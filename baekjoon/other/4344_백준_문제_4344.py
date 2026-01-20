# 백준 문제 4344
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/4344
# 작성자: 학생
# 작성일: 2026. 01. 20. 11:53:54

import sys
input = sys.stdin.readline

n = int(input())

def solve(n):
    ans_n = []
    cnt_list = []
    for i in range(n):
        t_list = list(map(int, input().split()))
        t = t_list[0]
        s_list = t_list[1:]
        avg_score = sum(s_list)/t
        cnt = 0
        for i in s_list:
            if i > avg_score:
                cnt += 1
        ans_n.append(t)
        cnt_list.append(cnt)
    for a,b in zip(ans_n,cnt_list):
        print(f'{100*b/a:.3f}%')

solve(n)