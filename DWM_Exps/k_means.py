import numpy as np
import math

dataset = [[180,98],[165,50],[170,89],[190,75],[185,62],[191,55],[176,90],[163,71],[184,59],[199,78]]

k=2
cluster1 =[]
cluster2 = []

centroid1 = [180,98]
centroid2 = [165,50]
iteration = 0

def kmeans():
    global centroid1,centroid2,cluster1,cluster2,iteration
    print("\nIteration", iteration+1)
    
    for i in range(0, len(dataset)):
        a = abs(math.sqrt(pow((centroid1[0]-dataset[i][0]), 2) + pow((centroid1[-1] - dataset[i][-1]), 2)))
        
        b= abs(math.sqrt(pow((centroid2[0] - dataset[i][0]), 2) + pow((centroid2[-1] - dataset[i][-1]) , 2)))
        
        print(a,b)
        
        if a>b:
            cluster2.append(dataset[i])
        else:
            cluster1.append(dataset[i])
            
        print(cluster1 , cluster2)
        
    listx1 = []
    listy1 = []

    for x,y in cluster1:
        listx1.append(x)
        listy1.append(y)
    x1 , y1 = listx1, listy1
    
    listx2 = []
    listy2 = []

    for x,y in cluster2:
        listx2.append(x)
        listy2.append(y)
    x2 , y2 = listx2 , listy2
    
    valx1 = sum(x1)/ len(x1)
    valy1 = sum(y1)/ len(y1)
    
    valx2 = sum(x2)/ len(x2)
    valy2 = sum(y2)/ len(y2)
    
    tup1 = (float("{:.2f}".format(valx1)), float("{:.2f}".format(valy1)))
    tup2 = (float("{:.2f}".format(valx2)), float("{:.2f}".format(valy2)))
    
    print("\n The mean centroids are \n",tup1,"\n",tup2)

    if tup1 == centroid1 and tup2 == centroid2:
        print("\n Clusters have been formed")
    
    else:
        centroid1=tup1
        centroid2 = tup2
        
        cluster1 = []
        cluster2 = []

        kmeans()
kmeans()