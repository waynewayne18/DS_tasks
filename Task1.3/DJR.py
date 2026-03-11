from collections import defaultdict
import pandas as pd
import heapq

rails = pd.read_csv("activity1_3_railnetwork_data.csv", header = None)

tv_middle = []
origin = rails.iloc[:, 0]
desti = rails.iloc[:, 1]
ori_to_dest = rails.iloc[:, 2]
dest_to_ori = rails.iloc[:, 3]

rw_dict = defaultdict(dict)

def addNodes(rw_dict, index):
    rw_dict[str(origin[index]).lower()][str(desti[index]).lower()] = ori_to_dest[index]
    rw_dict[str(desti[index]).lower()][str(origin[index]).lower()] = dest_to_ori[index]
    return -1
#print (json.dumps(dict(rw_dict), indent=4))

def dijkstra(start):
    heap = []
    visited = []
    unvisited = []
    current = start
    fill_unvisited(unvisited)
    rw_dict[start][start] = 0 #added cost orig -> orig = 0 so prev node cost + node cost works for first pass

    while len(visited) < len(unvisited):
        if current not in visited:
            visited.append(current)
        for nx_node in rw_dict[current]:
            if nx_node not in visited:
                heapq.heappush(heap, (rw_dict[current][nx_node] + rw_dict[start][current], nx_node)) #node[0] is cost, [1] is station 
        for node in heap:
            #print (node)
            if node[1] not in rw_dict[start] or (node[0] < rw_dict[start][node[1]]):
                if node[1] in rw_dict[current]:
                    rw_dict[start][node[1]] =  node[0]
        #print("visited", len(visited))
        c, current =heapq.heappop(heap)
        #print("current", current)
    return -1

def fill_unvisited(unvisited):
    for i in range(len(origin)):
        if origin[i] not in unvisited:
            unvisited.append(origin[i])

for i in range(len(origin)):
    addNodes(rw_dict, i)

#input("enter start station: ")
while 1 == 1:
    tv_origin = input("enter start station: ").lower()
    if tv_origin in rw_dict.keys():
        break
    else:
        print("enter valid station, check spelling and try again")
#input("enter end station: ")
while 1 == 1:
    tv_desti = input("enter end station: ").lower()
    if tv_desti in rw_dict.keys():
        break
    else:
       print("enter valid station, check spelling and try again")
#input("enter in between stations: ")
while 1 == 1:
    if input("enter 1 to stop adding stations, any other char to continue: ") == "1":
        break
    while 1 == 1:
        between = input("enter in between stations: ").lower()
        if between in rw_dict.keys():
            break
        else:
            print("enter valid station, check spelling and try again")
    tv_middle.append(between)

dijkstra(tv_origin)
#print(rw_dict[tv_origin])
for mid_stat in tv_middle:
    if mid_stat not in rw_dict[tv_origin]:
        print("middle station ", mid_stat ,  " is not connected to start station, aborting")
        exit()
    else:
        dijkstra(mid_stat)
        #print(rw_dict[mid_stat])
dijkstra(tv_desti)
print(rw_dict[tv_desti])
