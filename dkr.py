import re

import csv
import pandas

def sz(s):
    rea = re.compile("((?:\d)+(?:\.\d+)?)")

    s = s.replace(',', "", -1)
    r4 = rea.findall(s)
    if len(r4) > 0:
       return  float(r4[0])
    return  0


csv_reader1 = csv.reader(open('./csv/1.csv', 'r'))
csv_reader2 = csv.reader(open('./csv/2.csv', 'r'))
csv_reader3 = csv.reader(open('./csv/3.csv', 'r'))
csv_reader4 = csv.reader(open('./csv/4.csv', 'r'))

arr1 = []
arrMap1 = {}
arr2 = []
arrMap2 = {}
arr3 = []
arrMap3 = {}
arr4 = []
arrMap4 = {}
ind1 = 0
ind2 = 0
ind3 = 0
ind4 = 0
for row1 in csv_reader1:
    ind1 += 1
    if ind1 == 1:
        print(row1)
        continue
    if row1[3] == "":
        continue

    # print(float(row1[3]))
    # print(float(row1[4][1:]))
    row1[3] = sz(row1[3])
    row1[4] = sz(row1[4])
    row1[5] = sz(row1[5])
    # print(rea.search(row1[4]).string)
    # print(row1[5])
    row11 = row1[2:]
    arr1.append(row11)
    if row1[1] not in arrMap1:
        arrMap1[row1[1]] = []
    arrMap1[row1[1]].append(row11)

for row2 in csv_reader2:
    ind2 += 1
    if ind2 == 1:
        print(row2)
        continue
    if row2[3] == "":
        continue
    row2[3] = sz(row2[3])
    row2[4] = sz(row2[4])
    row2[5] = sz(row2[5])
    row22 = row2[2:]
    arr2.append(row22)
    if row2[1] not in arrMap2:
        arrMap2[row2[1]] = []
    arrMap2[row2[1]].append(row22)

for row3 in csv_reader3:
    ind3 += 1
    if ind3 == 1:
        print(row3)
        continue
    if row3[2] == "":
        continue
    row3[3] = sz(row3[3])
    row33 = row3[2:]
    arr3.append(row33)
    if row3[1] not in arrMap3:
        arrMap3[row3[1]] = []
    arrMap3[row3[1]].append(row33)

for row4 in csv_reader4:
    ind4 += 1
    if ind4 == 1:
        print(row4)
        continue
    if row4[2] == "":
        continue
    row4[3] = sz(row4[3])
    row44 = row4[2:]
    arr4.append(row44)
    if row4[1] not in arrMap4:
        arrMap4[row4[1]] = []
    arrMap4[row4[1]].append(row44)

dkr1 = []
for (k1,r1) in arrMap1.items():
        for (k3,r3) in arrMap3.items():
            for (k4,r4) in arrMap4.items():
                if k1 == k3 and k3 == k4:
                    for rr1 in r1:
                        for rr3 in r3:
                            for rr4 in r4:
                                arr = []
                                arr.extend(rr1)
                                arr.extend(rr3)
                                arr.extend(rr4)
                                dkr1.append(arr)



dkr2 = []
for (k2,r2) in arrMap2.items():
        for (k3,r3) in arrMap3.items():
            for (k4,r4) in arrMap4.items():
                if k2 == k3 and k3 == k4:
                    for rr2 in r2:
                        for rr3 in r3:
                            for rr4 in r4:
                                arr = []
                                arr.extend(rr2)
                                arr.extend(rr3)
                                arr.extend(rr4)
                                dkr2.append(arr)
mm1 = [{} for i in dkr2[0]]
i = -1
ind = 1
while i < len(dkr2) -1:
    i+=1

    j = -1
    while j < len(dkr2[0]) - 1:
        j += 1
        if len(mm1[j]) == 0:
            mm1[j] = {}
        if dkr2[i][j] == "":
            dkr2[i][j] = "0"
        if isinstance(dkr2[i][j] , int) or isinstance(dkr2[i][j] , float):
            continue


mm2 = [{} for i in dkr1[0]]
ind = 1
i = -1
while i < len(dkr1) -1:
    i+=1

    j = -1
    while j < len(dkr1[0]) - 1:
        j += 1
        if len(mm2[j]) == 0:
            mm2[j] = {}
        if dkr1[i][j] == "":
            dkr1[i][j] = "0"
        if isinstance(dkr1[i][j] , int) or isinstance(dkr1[i][j] , float):
            continue



name = ['Offer','Unit Price','USD Unit Price','Floor Difference','From','Expiration','Received' ,'name','pric','token','name','pric','token']

# name = ["index","name","time","coll","crea","favc","snss"]
test = pandas.DataFrame(columns=name, data=dkr1)
test.to_csv("./csv/v1dkr1.csv", encoding='utf-8',index=None)

# name = ["index","name","time","coll","crea","favc","snss"]
test = pandas.DataFrame(columns=name, data=dkr2)
test.to_csv("./csv/v1dkr2.csv", encoding='utf-8',index=None)


mm1 = [{} for i in dkr2[0]]
i = -1
ind = 1
while i < len(dkr2) -1:
    i+=1

    j = -1
    while j < len(dkr2[0]) - 1:
        j += 1
        if len(mm1[j]) == 0:
            mm1[j] = {}
        if dkr2[i][j] == "":
            dkr2[i][j] = "0"
        if isinstance(dkr2[i][j] , int) or isinstance(dkr2[i][j] , float):
            continue
        if dkr2[i][j] not in mm1[j]:
            mm1[j][dkr2[i][j]] = ind
            dkr2[i][j] = ind
            ind += 1
        else:
            dkr2[i][j] = mm1[j][dkr2[i][j]]

mm2 = [{} for i in dkr1[0]]
ind = 1
i = -1
while i < len(dkr1) -1:
    i+=1

    j = -1
    while j < len(dkr1[0]) - 1:
        j += 1
        if len(mm2[j]) == 0:
            mm2[j] = {}
        if dkr1[i][j] == "":
            dkr1[i][j] = "0"
        if isinstance(dkr1[i][j] , int) or isinstance(dkr1[i][j] , float):
            continue
        if dkr1[i][j] not in mm2[j]:
            mm2[j][dkr1[i][j]] = ind
            dkr1[i][j] = ind
            ind += 1
        else:
            dkr1[i][j] = mm2[j][dkr1[i][j]]


name = ['Offer','Unit Price','USD Unit Price','Floor Difference','From','Expiration','Received' ,'name','pric','token','name','pric','token']
test = pandas.DataFrame(columns=name, data=dkr1)
test.to_csv("./csv/dkr1.csv", encoding='utf-8',index=None)

name = ['Offer','Unit Price','USD Unit Price','Floor Difference','From','Expiration','Received' ,'name','pric','token','name','pric','token']
test = pandas.DataFrame(columns=name, data=dkr2)
test.to_csv("./csv/dkr2.csv", encoding='utf-8',index=None)