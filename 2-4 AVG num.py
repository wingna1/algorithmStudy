n = int(input())
num_list = list(map(int, input().split()))

avg_num = round(sum(num_list)/n)
temp = 0
answer = 0

for i in enumerate(num_list):
    if abs(avg_num-i[1]) < abs(avg_num-temp):
        temp = i[1]
        answer = i[0]+1
    elif  abs(avg_num-i[1]) == abs(avg_num-temp):
        # 점수가 높은 쪽이...
        if i[1] > temp:
            temp = i[1] 
            answer = i[0]+1 
        elif i[1] == temp:
            # 학생번호가 빠른 쪽이....
            if answer > i[0]:
                answer = i[0]
                temp = i[1]

print(avg_num, answer)
