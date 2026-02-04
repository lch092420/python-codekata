# 백준 문제 2609
# 백준 (unknown)
# 문제 링크: https://www.acmicpc.net/problem/2609
# 작성자: 학생
# 작성일: 2026. 02. 04. 19:39:35

import sys
input = sys.stdin.readline

#최소공배수, 최대공약수

a,b = map(int,input().split())

def gcb(x,y):
    cbx = []
    cby = []
    cb = []
    for i in range(1,x+1):
        if x%i ==0:
            cbx.append(i)
    for i in range(1,y+1):
        if y%i ==0:
            cby.append(i)
    if x <= y:
        for a in cbx:
            if a in cby:
                cb.append(a)
        return max(cb)
    else:
        for b in cby:
            if b in cbx:
                cb.append(b)
        return max(cb)

f = gcb(a,b)


def lcm(x,y):
    ans = f
    while (ans % x !=0) or (ans % y !=0):
        ans += f
    return ans

print(gcb(a,b),lcm(a,b),sep='\n')