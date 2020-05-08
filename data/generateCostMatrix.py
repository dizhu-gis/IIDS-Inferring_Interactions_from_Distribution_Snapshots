# *- coding: cp936 -*
#构建推算返乡流的成本矩阵
# 考虑城市的距离、吸引力因素

import numpy as np
import copy
# path='G:\\NightLightAndCheckIn\\'

# Distance coefficient
beta=0.8

# read distance matrix
distance=np.genfromtxt('Distance_Matrix.csv',delimiter=',',dtype=None)

# read node attractions
attraction=np.genfromtxt('NodeAttractions.txt',delimiter='\n',dtype=None)

# Ci_j=pow(distance,beta)/(Ai*Aj)
cost=copy.deepcopy(distance)

N=int(distance.shape[0])
for i in range(0,N):
    for j in range(0,N):
        # cost[i][j]=pow(10,9)*pow(float(distance[i][j]),beta)/(float(attraction[i])*float(attraction[j]))
        # cost[i][j]=pow(10,15)/(float(attraction[i])*float(attraction[j]))
        cost[i][j]=1
out= open("Cost_Matrix_equa.csv","w")
out.write(str(N)+'\n')
for i in range(0,N):
    for j in range(0,N):
        if j!=N-1:
            out.write(str(cost[i][j])+' ')
        else:
            out.write(str(cost[i][j])+'\n')

