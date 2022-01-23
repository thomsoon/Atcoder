S =  list(input())
a,b = list(map(int, input().rstrip().split()))

temp = S[a-1]
S[a-1] = S[b-1]
S[b-1] = temp


print("".join(S))