

"""
codeforce: https://codeforces.com/problemset/problem/2057/A

3
1 1
2 2
3 5
"""

n = int(input())
sizes = [list(map(int, input().split())) for _ in range(n)]

for size in sizes:
    print(f'{max(size[0], size[1])}\n')