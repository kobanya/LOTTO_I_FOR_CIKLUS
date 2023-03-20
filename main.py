'''
NB-2023.03.20
Lotto - for ciklussal
f kiíratás
'''


from random import *

for i in range(5):
    szam=randrange(90)+1
   # print(szam, end=' ')   # ird egy sorba, szóközzel a végén


    #print("%d" % szam, end=' ')

    #print(f" a szám:  {szam}", end=" ")

    print(f"  {i+1} .szám :   {szam}")

