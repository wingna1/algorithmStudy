T = int(input())
cnt = 0

while cnt < T:
    n,s,e,k = map(int, input().split())
    seq = list(map(int, input().split()))
    seq_list = seq[s-1:e]
    seq_list.sort()
    cnt += 1
    print(seq_list[k-1])
