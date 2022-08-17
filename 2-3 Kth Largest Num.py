n,k = map(int, input().split())
num_list = list(map(int, input().split()))
answer = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            answer.add(num_list[i] + num_list[j] + num_list[m])

print(sorted(list(answer), reverse=True)[k-1])
