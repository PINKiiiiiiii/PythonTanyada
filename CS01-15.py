score = []
while(score != -1):
    x = int(input("input your scores : "))
    if x == -1:
        break
    score += [x]

for i in score:
    print(i)