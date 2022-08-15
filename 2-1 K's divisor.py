# K번째 약수 

n, k = map(int, input().split())
divisor = [ i for i in range(1, n+1) if n%i == 0 ]

if len(divisor) < k :
    print(-1)
else:
    print(divisor[k-1])

# 리스트를 사용하는 것은 k번째 약수를 찾은 후에도 진행되므로
# 비효율적이다. cnt를 사용해 검증하면서 break를 사용하는 것이 효율적.