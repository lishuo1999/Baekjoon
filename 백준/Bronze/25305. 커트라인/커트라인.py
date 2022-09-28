from sys import stdin
a, b = map(int, stdin.readline().split())
result = stdin.readline().split()
result = list(map(int, result))
result.sort(reverse=True)
print(result[b-1])