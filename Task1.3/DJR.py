import sys
from collections import defaultdict
import pandas as pd
import json
import heapq

rails = pd.read_csv("activity1_3_railnetwork_data.csv", header = None)

tv_middle = []
origin = rails.iloc[:, 0]
desti = rails.iloc[:, 1]
ori_to_dest = rails.iloc[:, 2]
dest_to_ori = rails.iloc[:, 3]
heap = []
heapq.heapify(heap)

rw_dict = defaultdict(dict)
unvisited = []
visited = []

def addNodes(rw_dict, index):
    rw_dict[origin[index]][desti[index]] = ori_to_dest[index]
    rw_dict[desti[index]][origin[index]] = dest_to_ori[index]
    return -1
#print (json.dumps(dict(rw_dict), indent=4))

def dijkstra(start):
    start = start
    current = start
    while len(visited) < len(unvisited):
        if current not in visited:
            visited.append(current)
        for nx_node in rw_dict[current]:
            if nx_node not in visited:
                heapq.heappush(heap, (rw_dict[current][nx_node], nx_node)) #node[0] is cost, [1] is station 
        for node in heap:
            #print (node)
            if node[1] not in rw_dict[start] or (node[0] + rw_dict[start][current] < rw_dict[start][node[1]]):
                rw_dict[start][node[1]] =  node[0] + rw_dict[start][current]
        #print("visited", len(visited))

        c, current =heapq.heappop(heap)
        #print("current", current)
    return -1

#input("enter start station: ")
while 1 == 1:
    tv_origin = input("enter start station: ")
    if tv_origin in origin.values:
        break
    else:
        print("enter valid station, check spelling and try again")
#input("enter end station: ")
while 1 == 1:
    tv_desti = input("enter end station: ")
    if tv_desti in desti.values:
        break
    else:
       print("enter valid station, check spelling and try again")
#input("enter in between stations: ")
while 1 == 1:
    if input("enter 1 to stop adding stations, any other char to continue: ") == "1":
        break
    while 1 == 1:
        between = input("enter in between stations: ")
        if between in origin.values or between in desti.values:
            break
        else:
            print("enter valid station, check spelling and try again")
    tv_middle.append(between)

for i in range(len(origin)):
    if origin[i] not in unvisited:
        unvisited.append(origin[i])

for i in range(len(origin)):
    addNodes(rw_dict, i)
print(rw_dict["London"])
rw_dict[tv_origin][tv_origin] = 0 #added cost orig -> orig = 0 so line 68 works
dijkstra(tv_origin)
print (rw_dict[tv_origin])