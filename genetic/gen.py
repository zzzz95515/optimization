import random as r
import numpy as np

x = 10000
lastbest=''
schet = np.zeros(x)
slovar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-.,!:;?«»— "

target = "Пусть я был смешон в Ваших глазах и в глазах Вашегобрата, " \
         "Николая Николаевича.Уходя, я в восторге говорю:«Да святится имя Твое»."
le = len(target)
pop = []
bestsch = 0


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


# создание первого поколения

for i in range(x):
    stri = []
    for j in range(le):
        symb = slovar[r.randint(0, len(slovar) - 1)]
        stri.append(symb)
    pop.append(stri)
# подсчет и поиск совпадений
for i in range(x):
    for j in range(le):
        if (target[j] == pop[i][j]):
            schet[i] += 1
# поиск лучшего элемента
maximum = -1
for i in range(x):
    if (maximum < schet[i]):
        maximum = schet[i]
        maxi = i
best = pop[maxi]
bestsch = schet[maxi]
while (bestsch < le):
    for i in range(x):
        schet[i] = 0
        if (i > x / 2):
            pop[i] = mutation(slovar, pop[i], le,bestsch)
        else:
            pop[i] = skresh(best, pop[i], le)
        for j in range(le):
            if (target[j] == pop[i][j]):
                schet[i] += 1
    for i in range(x):
        if (schet[i] > bestsch):
            bestsch = schet[i]
            best = pop[i]
print("best=", best, '   bestsch=', bestsch)