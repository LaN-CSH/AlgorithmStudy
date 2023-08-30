a = input()
a = a.split()
d = list(map(int, a))
b = [d[0], d[1], 0, 0]

b[2]=abs(d[2]-d[0])
b[3]=abs(d[3]-d[1])

print(min(b))
