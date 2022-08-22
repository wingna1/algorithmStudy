n, m = map(int, input().split())
result_dict = {}
possible_list = set()

for i in range(1, n+1):
    for j in range(1, m+1):
        temp = i + j
        if temp not in possible_list:
            possible_list.add(temp)
            result_dict[temp] = 0
        else:
            result_dict[temp] = result_dict[temp]+1

max_value = max(result_dict.values())

for k, v in result_dict.items():
    if v == max_value:
        print(k, end=' ')
