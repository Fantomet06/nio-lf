key = str(input())
key = list(key)

L = int(input())

msg = str(input())
msg = list(msg)

a = []

for i in range(L):
    b = msg[i]
    c = key.index(b)
    try:
        a.append(key[c-1])
    except:
        a.append(key[-1])

print("".join(a))