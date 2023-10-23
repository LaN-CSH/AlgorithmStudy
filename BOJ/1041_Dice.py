n = int(input())
dice_num = list(map(int, input().split()))

if n>=2:
  min1 = min(dice_num)
  min2_list = []
  min3_list = []
  for i in range(6):
    for j in range(6):
      if (i+j)!=5 and i!=j:
        min2_list.append(dice_num[i]+dice_num[j])
        
  min2 = min(min2_list)
  
  
  for i in range(6):
    for j in range(6):
      for k in range(6):
        if (i+j!=5 and i!=j) and (i+k!=5 and i!=k) and (j+k!=5 and j!=k):
          min3_list.append(dice_num[i]+dice_num[j]+dice_num[k])
  
  min3 = min(min3_list)
  
  result = (5*(n**2)-16*n+12)*min1 + (8*n-12)*min2 + 4*(min3)
  print(result)
elif n == 1:
  print(sum(dice_num)-max(dice_num))
