
"""
3
1 1 0
1 1 1
1 0 0
"""

n = input() # this will be indicating number of lines for input
print([1 if input().split().count('1') >= 2 else 0 for _ in range(int(n))].count(1))