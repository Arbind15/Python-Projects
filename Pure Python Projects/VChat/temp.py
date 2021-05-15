# code
T = int(input())
for y in range(T):
    X = int(input())
    Dict = input()
    Str = input()
    freq = []
    i = 0
    for itm1 in Dict.split():
        for itm3 in itm1:
            for itm2 in Str:
                if (itm3 == itm2):
                    i = i + 1
        freq.append(i)
        i = 0

    Max = max(freq)
    Max = freq.index(Max)
    print(Dict.split()[Max])





