

n = int(input())
words = [word[0]+str(len(word)-2)+word[-1] if len(word) > 10 else word for word in (input() for _ in range(n))]
for word in words:
    print(word+'\n')