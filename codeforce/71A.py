

n = int(input())
words = list(map(
    lambda s:s[0]+(len(s) - 2)+s[-1] if(len(s) > 10) else s,
    [input() for _ in range(n)]
))

for word in words:
    print(word+'\n')