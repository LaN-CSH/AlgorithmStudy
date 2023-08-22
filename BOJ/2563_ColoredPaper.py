num_papers_ = int(input())
whole_area_ = [[0]*100 for _ in range(100)]

sum1 = 0

paper_coordinate = []
for i in range(num_papers_):
    x_, y_ = list(map(int, input().split(' ')))
    for j in range(10):
        for k in range(10):
            whole_area_[x_+j][y_+k] = 1
    paper_coordinate.append([x_, y_])
for l in range(100):
    sum1 += sum(whole_area_[l])
#     print(sum(whole_area_[l]))
#     print(whole_area_[l])
print(sum1)
