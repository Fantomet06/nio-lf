N,M,I,S = map(int, input().split())
møter = []
folk = [0]

ints = [I]
inte = [I+S-1] #noen problemer med disse listene

for i in range(M):
    o,p,j = map(int, input().split())
    møter.append([o, p, j])
for i in range(N-1):
    folk.append('f')
møter.sort(key=lambda x: int(x[2]))

# fase 2, intervallorganisering
for i in range(M):
    day = møter[i][2]
    person0 = møter[i][0]
    person1 = møter[i][1]


    try:
        if folk[person0]+I+S > day and folk[person0]+I <= day and folk[person1] == 'f':
            folk[person1] = day
            ints.append(day+I)
            inte.append(day+I+S-1)
    except:
        pass
    try:
        if folk[person1]+I+S > day and folk[person1]+I <= day and folk[person0] == 'f':
            folk[person0] = day
            ints.append(day+I)
            inte.append(day+I+S-1)
    except: 
        pass
def maxsyk(startint, lastint, n):


    startint.sort()
    lastint.sort()


    sykenå = 1
    max_syke = 1
    i = 1
    j = 0


    while (i < n and j < n):
        if (startint[i] <= lastint[j]):
            sykenå += 1

            if(sykenå > max_syke):
        
                max_syke = sykenå

            i += 1
    
        else:
            sykenå -= 1
            j += 1
    
    print(max_syke)


maxsyk(ints, inte, len(ints))