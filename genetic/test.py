import random as r

import numpy as np

slovar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-.,!:;?«»— "
targett = "Пусть я был смешон в Ваших глазах и в глазах Вашего брата, " \
         "Николая Николаевича. Уходя, я в восторге говорю:«Да святится имя Твое»."
def mutation(slovar, subj, le, bestsch):
    for i in range (int(le-bestsch)):
        k = r.randint(0, le - 1)
        c = r.randint(0, len(slovar) - 1)
        subj[k] = slovar[c]
    return subj


def skresh(best, subj, le):
    k = r.randint(0, le - 1)
    subj[k] = best[k]
    return subj

def first(slovar,le,x):
    pop=[]
    for i in range(x):
        stri = []
        for j in range(le):
            symb = slovar[r.randint(0, len(slovar) - 1)]
            stri.append(symb)
        pop.append(stri)
    return pop


target=targett.split(" ")
pop=[]
x=100000
schet=np.zeros((len(target),x))
best = []
bestsch=np.zeros(len(target))
for i in range(len(target)):
    pop.append(first(slovar,len(target[i]),x))
for i in range (len(target)):
    for j in range (x):
        for n in range (len(target[i])):
            if (pop[i][j][n]==target[i][n]):
                schet[i][j]+=1
    maxim=-1
    maxj=0
    for j in range (x):
        if (maxim<schet[i][j]):
            maxim=schet[i][j]
            maxj=j
    best.append(pop[i][maxj])
    bestsch[i]=maxim
for i in range(len(target)):
    fraza=''
    while (bestsch[i]<len(target[i])):
        schet = np.zeros((len(target), x))
        for j in range(x):
            schet[i][j] = 0
            if (j > x / 2):
                pop[i][j] = mutation(slovar, pop[i][j], len(target[i]), bestsch[i])
            else:
                pop[i][j] = skresh(best[i], pop[i][j], len(target[i]))
            for n in range(len(target[i])):
                if (target[i][n] == pop[i][j][n]):
                    schet[i][j] += 1
        for j in range(x):
            if (schet[i][j] > bestsch[i]):
                bestsch[i] = schet[i][j]
                best[i] = pop[i][j]
    for k in range(len(target)):
        for j in range(len(target[k])):
            fraza += best[k][j]
        fraza += ' '
    print(fraza)