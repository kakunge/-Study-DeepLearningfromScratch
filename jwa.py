import numpy as np
import random as ran

#좌표 설정
w, d, h = map(int, input().split())
arr = np.empty((w, d), int)

for i in range(w):
        for j in range(d):
            arr[i, j] = ran.randint(0, h)

rw, rd = ran.randint(0, w-2), ran.randint(0,d-2)
r = ran.randint(0, h)
arr[rw, rd] = arr[rw, rd+1] = arr[rw+1, rd] = arr[rw+1, rd+1] = r

'''
print(rw, rd, r)
print(np.max(arr))
print(arr)
'''

#드론 좌표 설정
dw1 = ran.randint(0, w-2)
dd1 = ran.randint(0, d-2)
dw2 = dw1+1
dd2 = dd1
dw3 = dw1
dd3 = dd1+1
dw4 = dw1+1
dd4 = dd1+1
dh = ran.randint(h+1, h+60)

#print(dw1, dd1, dh)

#인식 가능 구역
ch = np.zeros((w, d))

#평면 거리 계산
distanceArr = np.zeros((w, d), float)
distance = 0

def dis(x, y):
    cx = (abs(dw4-x))**2
    cy = (abs(dd4-y))**2
    if x == dw4:
        cx = (abs(dw4+1-x))**2
        cy = (abs(dd4-y))**2
    elif y == dd4:
        cx = (abs(dw4-x))**2
        cy = (abs(dd4+1-y))**2
    elif x == dw4 and y == dd4:
        pass
    d = (cx+cy)
    return d

for i in range(w):
    for j in range(d):
        distance = dis(i, j)
        distanceArr[i, j] = distance

distanceArr[dw1, dd1] = 0.0
distanceArr[dw2, dd2] = 0.0
distanceArr[dw3, dd3] = 0.0
distanceArr[dw4, dd4] = 0.0

distanceArr = np.sqrt(distanceArr, distanceArr)

#print(distanceArr)

#기울기 계산
slopeArr = np.zeros((w, d), float)
slope = 0

def slp(x, y):
    s = abs((dh-arr[x, y])/distanceArr[x, y])
    return s

for i in range(w):
    for j in range(d):
        slope = slp(i, j)
        slopeArr[i, j] = slope

slopeArr[dw1, dd1] = 0.0
slopeArr[dw2, dd2] = 0.0
slopeArr[dw3, dd3] = 0.0
slopeArr[dw4, dd4] = 0.0
        
print(slopeArr)

#탐색 가능한 영역 구분
def find(l):
    min = 10**98
    lp=[]
    for i in range(len(l)):
        if min > l[i]:
            min = l[i]
            lp.append(min)

    return lp

