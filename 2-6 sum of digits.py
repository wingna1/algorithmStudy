n = int(input())
num_list = list(map(int, input().split()))
max_num = 0
idx = 0

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

for x, y in enumerate(num_list):
    sum = digit_sum(y)
    if sum > max_num:
        max_num = sum
        idx = x

print(num_list[idx])