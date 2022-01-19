def intList(l):
    return [int(e) for e in l]

debug = False
if debug:
    inbyggere, ntreff, inkubasjon, sykdom = 5, 14, 3, 5
    orgTreff = [[0, 1, 0], [0, 2, 1], [3, 0, 1], [4, 0, 2], [0, 1, 3], [1, 2, 3], [0, 4, 4], [0, 2, 8], [0, 3, 8], [1, 2, 10], [3, 4, 10], [3, 0, 14], [3, 1, 15], [3, 4, 16]]

else:
    inbyggere, treff, inkubasjon, sykdom = input().split(' ')
    inbyggere, ntreff, inkubasjon, sykdom = int(inbyggere), int(treff), int(inkubasjon), int(sykdom)
    orgTreff = [intList(input().split(' ')) for i in range(ntreff)]

def getThird(l):
    return l[2]

def getFirst(l):
    return l[0]

orgTreff.sort(key=getThird)

def smittsom(p, dag):
    p = befolkning[p]
    return p[0] <= dag < p[1]

befolkning = [[-2, -2, False] for i in range(inbyggere)]
#Smitte person 0
befolkning[0][2] = True
befolkning[0][0] = inkubasjon
befolkning[0][1] = inkubasjon + sykdom

#Starte loggen, med person 0
smitteLogg = []
smitteLogg += [[inkubasjon, 1]]
smitteLogg += [[inkubasjon + sykdom, -1]]

if orgTreff == []:
    #Ingen treff = bare pasient 0 blir smittet
    print(1)

else:
    def checkInfected(dagN):
        for p in befolkning:
            if dagN < p[1]:
                return False

        return True

    c = 0
    pågående = []

    for treff in orgTreff:
        dagN = treff[2]

        if dagN % 10000 == 0:
            #Dersom ingen er smitsomme, burde vi avbryte. Sjekker en gang i blant
            if checkInfected(dagN):
                break

        smittetPerson = None
        if (not befolkning[treff[1]][2]) and smittsom(treff[0], dagN):
            smittetPerson = befolkning[treff[1]]


        elif (not befolkning[treff[0]][2]) and smittsom(treff[1], dagN):
            smittetPerson = befolkning[treff[0]]

        if smittetPerson != None:
            smittetPerson[2] = True
            smittetPerson[0] = dagN + inkubasjon
            smittetPerson[1] = smittetPerson[0] + sykdom

            smitteLogg += [[dagN + inkubasjon, 1]]
            smitteLogg += [[dagN + inkubasjon + sykdom, -1]]


    c = 0
    largest = 0

    smitteLogg.sort(key=getFirst)

    for l in smitteLogg:
        c += l[1]
        if c > largest:
            largest = c


    if debug:
        print(largest, smitteLogg)
        if smitteLogg == [0, 0, 0, 1, 1, 1, 2, 3, 2, 2, 2, 1, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0]:
            print('yay')
        else:
            print('buuuh')

    else:
        print(largest)
