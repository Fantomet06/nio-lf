N = int(input())
list = []

for i in range(N):
    list.append(int(input()))

list.sort()

for x in range(len(list)):
    try:
        try:
            if list[x] != list[x+1] and list[x] != list[x-1]:
                answer = list[x]
                break
        except:
            if list[x] != list[x+1]:
                answer = list[x]
                break
    except:
        if list[x] != list[x-1]:
            answer = list[x]
        else:
            answer = -1

print(answer)