S = list(input())
count = 0
max_c = 0
for i in S:
    if i == "A" or i == "C" or i == "G" or i == "T":
        count += 1
    else:
        max_c = max(count,max_c)
        count = 0
max_c = max(count,max_c)
print(max_c)