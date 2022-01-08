N , K = list(map(int, input().rstrip().split()))
P = list(map(int, input().rstrip().split()))


for i in range(K, N+1):
    set_p = set(P[:i])
    list_p = list(set_p)
    print(list_p[len(list_p)-K])