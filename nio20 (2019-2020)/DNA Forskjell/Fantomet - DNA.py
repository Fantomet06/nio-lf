# !! DENNE KODEN GIR BARE 19 POENG !!

def main():
    N, M = map(int, input().split())

    word1 = str(input())
    word2 = str(input())

    l1 = list(word1)
    l2 = []
    b = 0

    for y in range(N):
        for i in range(N):
            try:
                check = [l1[x+y] for x in range(i+1)]
            except:
                pass
            check2 = "".join(check)
            if check2 not in word2:
                l2.append(check2)
                b += 1
    
    if b == 0:
        print("ingen")
    else:
        print(min(l2, key=len))
main()

