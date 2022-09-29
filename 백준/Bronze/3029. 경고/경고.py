from sys import stdin
a = stdin.readline().rstrip('\n').split(':') #현재시간
b = stdin.readline().rstrip('\n').split(':') #던질시간
#b-a
a = list(map(int, a))
b = list(map(int, b))
time_a = 3600*a[0]+60*a[1]+a[2] #초로 변환
time_b = 3600*b[0]+60*b[1]+b[2]
if time_a >= time_b: #하루를 더해야함
    time_b += 24*3600
h = int((time_b-time_a)/3600)
m = int((time_b-time_a)%3600/60)
s = (time_b-time_a)%3600%60
print('%02d:%02d:%02d' %(h, m, s))