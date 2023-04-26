def fermeture(A, x, n, m):
    ch = A[0][x]
    v = len(A[1]) * [1]

    for i in range(n):  # find the characters that have one in the same place as the current character
        for j in range(m):
            if i != 0:
                if x != j:
                    if A[i][x] == 1:
                        if A[i][j] != A[i][x]:
                            v[j] = 0
    for i in range(len(v)):
        if x != i:
            if v[i] == 1:
                ch = ch + A[0][i]
    print("Fermeture:", ch)
    return ch


def support(ch, A, m):  #Calculate the occ number in ch
    v = len(A[1]) * [1]
    for i in range(m):
        if A[0][i] not in ch:
            v[i] = 0
    tmp = []
    for i in range(len(v)):
        if v[i] == 1:
            tmp.append(i)
    cpt = 0
    for i in range(1, len(A)):
        if A[i][tmp[0]] == 1:
            bool = True
            for j in range(1, len(tmp)):
                if A[i][tmp[0]] != A[i][tmp[j]]:
                    bol = False
            if bool:
                cpt = cpt + 1
    return cpt


#find the fermuture of the 2nd itemset
def fermeture2(ch, A):
    m = len(A[1])
    v = len(A[1]) * [1]
    for i in range(m):
        if A[0][i] not in ch:
            v[i] = 0
    tmp = []
    tmp1 = []
    for i in range(len(v)):
        if v[i] == 1:
            tmp.append(i)
    for i in range(len(v)):
        if v[i] != 1:
            tmp1.append(i)
    res = []
    for i in range(1, len(A)):
        if A[i][tmp[0]] == 1:
            bool = True
            for j in range(1, len(tmp)):
                if A[i][tmp[0]] != A[i][tmp[j]]:
                    bool = False
            if bool:
                res.append(i)
    for i in range(len(tmp1)):
        bool = True
        for j in range(len(res)):
            if A[res[j]][tmp1[i]] != 1:
                bool = False
        if bool:
            ch = ch + A[0][tmp1[i]]
    return ch


def is_frequent(A, minsupport):
    bool = True
    for i in range(len(A)):
        if A[i][1] < minsupport:
            bool = False
    return bool


def prefixe(ch):
    return ch[0:len(ch) - 1]


def ferm(item, G):  
    for i in range(len(G)):
        if item == G[i][0]:
            return G[i][2]
    return -1


def concatenate(ch, ch1):
    for i in ch1:
        if i not in ch:
            ch = ch + i
    return ch


def inclus(item, ch):
    cpt = len(item)
    for i in item:
        if i in ch:
            cpt = cpt - 1
    if cpt == 0:
        return 0
    else:
        return 1

def difference(x, y):
    ch = ""
    for i in x:
        if i not in y:
            ch = ch + i
    for j in y:
        if j not in x:
            ch = ch + j
    return ch


def associations(minsupport, G):
    M = []
    for i in range(len(G)):

        if G[i][1] >= minsupport:
            M.append([G[i][0], difference(G[i][2], G[i][0])])

    return M


def close(minsupport, mat):
    n = len(mat)
    m = len(mat[1])

    v = m * [0]
    minsupport = minsupport / (n - 1)

    for i in range(n):
        for j in range(m):
            if i != 0:
                if mat[i][j] == 1:
                    v[j] = v[j] + 1

    #To avoid referenced before assignement later on
    Gen1 = []
    isFrequent1 = False
    assocs1 = []
    Gen2 = []
    isFrequent2 = False
    assocs2 = []
    Gen3 = []
    isFrequent3 = False
    assocs3 = []
    fermetureArray = []
    # La recherche des fermetures pour chaque item 
    for i in range(m):
        ch = fermeture(mat, i, n, m)
        fermetureArray.append(ch)
        # support(x) = freq(x)/D
        Gen1.append([mat[0][i], v[i] / (n - 1), ch])

    print("GEN-1")
    print(Gen1)
    print("Les associations de  GEN-1 :")

    #Extracting association rules
    assocs1 = associations(minsupport, Gen1)
    print(associations(minsupport, Gen1))
    print("minsupport:", minsupport)

    isFrequent1 = is_frequent(Gen1, minsupport)
    if not isFrequent1:
        print("done!")  #we stop when the last itemset is not frequent
    else:
        Gen2 = []
        for i in range(len(Gen1)):
            if Gen1[i][1] >= minsupport:
                for j in range(i, len(Gen1)):
                    if i != j:
                        if Gen1[j][1] >= minsupport:

                            if (Gen1[i][0] not in Gen1[j][2]) and (
                                    Gen1[j][0] not in Gen1[i][2]):  #in order to avoid redunduncy

                                y = support(Gen1[i][0] + Gen1[j][0], mat, m)

                                ch1 = fermeture2(Gen1[i][0] + Gen1[j][0],
                                                 mat)  # search the fermeture of the 2nd itmeset found

                                Gen2.append([Gen1[i][0] + Gen1[j][0], y / (n - 1), ch1])

        isFrequent2 = is_frequent(Gen2, minsupport)
        assocs2 = associations(minsupport, Gen2)
        
        if not isFrequent2:
            print("done!2")
        else:
            print("GEN2:\n")
            print(Gen2)
            print("associations : ")
            print(associations(minsupport, Gen2))
            compteur = 3
            # k = 3, il faut 2 éléments de taille k-1 qui ont k-2 prefixes commun et qui ne sont pas inclus dans leurs fermetures
            while True:
                temp = []
                for i in range(len(Gen2)):
                    if Gen2[i][1] >= minsupport:
                        for j in range(i, len(Gen2)):
                            if i != j:
                                if Gen2[j][1] >= minsupport:
                                    if prefixe(Gen2[i][0]) == prefixe(Gen2[j][0]):
                                        if (inclus(Gen2[i][0], ferm(Gen2[j][0], Gen2)) == 1) and (
                                                inclus(Gen2[j][0], ferm(Gen2[i][0], Gen2)) == 1):
                                            temp = [concatenate(Gen2[i][0], Gen2[j][0]),
                                                    support(concatenate(Gen2[i][0], Gen2[j][0]), mat, m) / (n - 1),
                                                    fermeture2(concatenate(Gen2[i][0], Gen2[j][0]), mat)]
                                            Gen3.append(temp)
                isFrequent3 = is_frequent(Gen3, minsupport)
                assocs3 = associations(minsupport, Gen3)
                if isFrequent3:
                    print(" Resultat final dans la" + str(compteur) + "ème itération")
                    print(Gen3)
                    print("Les associations :")
                    print(associations(minsupport, Gen3))
                    break
                else:
                    print(Gen3)
                    compteur = compteur + 1
                    Gen2 = Gen3
    return fermetureArray, Gen1, assocs1, minsupport, isFrequent1, Gen2, isFrequent2, assocs2, Gen3, isFrequent3, assocs3
