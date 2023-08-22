import math
N = math.ceil(math.log(int(input()),3))
def a(n):
  if n == 0: return ['*']
  elif n == 1: return ['***','* *','***']
  y = [3*i for i in a(n-1)]
  z = [k+" "*3**(n-1)+k for k in a(n-1)]
  return y+z+y
for j in a(int(N)):
  print(j)
