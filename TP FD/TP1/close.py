import numpy as np

def fermeture(mat,x,n,m):
    ch = mat[0][x] #get the character
  
    v = len(mat[1]) * [1] # v = [1,1,1,1,1]
    
    for i in range(n): # find the characters that have ONES in the same place as the current character ( closure of B is BA for ex)
        for j in range(m):
            if i!=0: # pour éviter le character
                if x!=j:
                    if mat[i][x]==1:
                        if mat[i][j]!=mat[i][x]:
                            v[j]=0                  
    for i in range(len(v)):
        if x!=i:
            if v[i] == 1:
                ch = ch + mat[0][i]  #concatenation
    print("ferm:", ch)
    return ch





def support(ch,A,m): #calculé le nombre d'occurences de la chaine ch
    v = len(A[1]) * [1]
    for i in range(m):
        if A[0][i] not in ch:
            v[i]=0
    tmp = []
    for i in range(len(v)):
        if v[i]==1:
            tmp.append(i)
    cpt =0
    for i in range(1,len(A)): 
        if A[i][tmp[0]]==1:
            bol = True
            for j in range(1,len(tmp)):
                if A[i][tmp[0]] != A[i][tmp[j]]:
                    bol = False
            if bol == True:
                cpt = cpt+1
    return cpt




#trouver la fermuture de les 2-itemset 
def fermeture2(ch,A):
    m = len(A[1])
    v = len(A[1]) * [1]
    for i in range(m):
        if A[0][i] not in ch: # pour qu'il rest seulement les 2 charact correspondant
            v[i]=0
    tmp = []
    tmp1 = []
    for i in range(len(v)):
        if v[i]==1:
            tmp.append(i) #contient les indices des charactères correspondant
    for i in range(len(v)):
        if v[i]!=1:
            tmp1.append(i) # contient les indies des autres carac
    res = []
    for i in range(1,len(A)): 
        if A[i][tmp[0]]==1:
            bol = True
            for j in range(1,len(tmp)):
                if A[i][tmp[0]] != A[i][tmp[j]]:
                    bol = False
            if bol == True:
                res.append(i)
    for i in range(len(tmp1)):
        bol = True
        for j in range(len(res)):
            if A[res[j]][tmp1[i]]!=1:
                bol = False
        if bol == True:
            ch = ch+A[0][tmp1[i]]
    return ch





def test(A,minsupport):
    bol = True
    
    for i in range(len(A)):
        if A[i][1]<minsupport:
            bol = False
    return bol




def prefixe(ch):
    return ch[0:len(ch)-1]



def ferm(item,G): #
    for i in range(len(G)):
        if item==G[i][0]:
            return G[i][2]
    return -1 



def concat(ch,ch1): #concatenation: AC + AE = ACE
    for i in ch1:
        if i not in ch:
            ch=ch+i
    return ch



def inclus(item,ch):
    cpt = len(item)
    for i in item:
        if i in ch:
            cpt = cpt -1
    if cpt == 0 :
        return 0
    else:
        return 1 




#trouver la différence entre deux chaines pour construire les régles d'associations
def difference(x,y):
    ch=""
    for i in x:
        if i not in y:
            ch=ch+i
    for j in y:
        if j not in x:
            ch=ch+j
    return ch



#affichages des associations des itemsets frequents
def associations(minsupport,G):
    M=[]
    for i in range(len(G)):
        
        if G[i][1]>=minsupport:    
            M.append([G[i][0],difference(G[i][2],G[i][0])])
    
    return M



def close(minsupport):
    mat=[["A","B","C","D","E"],[1,1,1,1,1],[1,1,0,0,0],[0,0,1,0,1],[1,1,0,1,1],[1,0,1,1,0]]
    
    
    n=len(mat)
    m=len(mat[1])

    v = m * [0]
    minsupport=minsupport/(n-1) #minsupport/5
    
    ## Cette boucle permet de calculer l'apparition de 1 pour chaque item ##
    # v va contenir les nombres d'apparitions de chaque charactere
    for i in range(n):
        for j in range(m):
            if i!=0 :
                if mat[i][j]==1 :
                    v[j]=v[j]+1  
    
    
    Gen1 = []
  


    ## La recherche des fermetures pour chaque item ##
    for i in range(m):
        ch = fermeture(mat,i,n,m)            
          #support(x) = freq(x)/D
        Gen1.append([mat[0][i],v[i]/(n-1),ch])
    
    print("GEN-1")
    print(Gen1)
    print("Les associations de  GEN-1 :")

    #extracting association rules
    print(associations(minsupport,Gen1))   #generator -> closed itemsets - generator
    print("minsupport:",minsupport)



    if test(Gen1,minsupport) == False:
        print("done!")
    else: 
        verif = test(Gen1,minsupport)
        Gen2= []
        tmp1 = []
        for i in range(len(Gen1)):
            if Gen1[i][1]>=minsupport:
                for j in range(i,len(Gen1)):
                    if i !=j:
                        if Gen1[j][1]>=minsupport:

                            if (Gen1[i][0] not in Gen1[j][2]) and (Gen1[j][0] not in Gen1[i][2]): #pour eviter les redondances
                                
                                y = support(Gen1[i][0]+Gen1[j][0],mat,m)
                                
                                ch1 = fermeture2(Gen1[i][0]+Gen1[j][0],mat) #trouver la fermuture de la 2-itemset trouvé
                                
                                Gen2.append([Gen1[i][0]+Gen1[j][0],y/(n-1),ch1])
        
        verif = test(Gen2,minsupport)
        if verif == False:
            print("done!")
            print(Gen2)
            print("associations :")
            print(associations(minsupport,Gen2))
        else:
            print("GEN2:\n")
            print(Gen2)
            print("associations : ")
            print(associations(minsupport,Gen2))
            k=3
            # k = 3, il faut 2 éléments de taille k-1 qui ont k-2 prefixes commun et qui ne sont pas inclus dans leurs fermetures
            while True:
                Gen3 = []
                temp = []
                for i in range(len(Gen2)):
                        if Gen2[i][1]>=minsupport:
                            for j in range(i,len(Gen2)):
                                if i !=j:
                                    if Gen2[j][1]>=minsupport:
                                        if prefixe(Gen2[i][0])==prefixe(Gen2[j][0]):
                                            if (inclus(Gen2[i][0] ,ferm(Gen2[j][0],Gen2))==1) and (inclus(Gen2[j][0] ,ferm(Gen2[i][0],Gen2))==1):
                                                temp= [concat(Gen2[i][0],Gen2[j][0]),support(concat(Gen2[i][0],Gen2[j][0]),mat,m)/(n-1),fermeture2(concat(Gen2[i][0],Gen2[j][0]),mat)]
                                                Gen3.append(temp)
                verif = test(Gen3,minsupport)
               
                if verif == True:
                    print(" Resultat final dans la" +str(k)+"ème itération")
                    print(Gen3)
                    print("Les associations :")
                    print(associations(minsupport,Gen3))
                    break
                else:
                    print(Gen3)
                    k=k+1
                    Gen2=Gen3




minsupport=int(input("enter Minsup: "))
close(minsupport)

