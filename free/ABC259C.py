S = input()
T = input()

j = 0
for i in range(len(T)):
    if S[j] != T[i]:
        if j >= 2 and S[j-2] == T[i]:
            pass
        else:
            print("No")
            exit()
    else:
        if j < len(S)-1:
            j += 1

print("Yes")