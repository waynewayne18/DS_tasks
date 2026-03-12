from collections import defaultdict
import pandas as pd
import heapq
from itertools import permutations
rails = pd.read_csv("activity1_3_railnetwork_data.csv", header = None)

middle_dicts = []
middle_nodes = []
origin = rails.iloc[:, 0]
desti = rails.iloc[:, 1]
ori_to_dest = rails.iloc[:, 2]
dest_to_ori = rails.iloc[:, 3]

rw_dict = defaultdict(dict)

def addNodes(rw_dict, index):
    rw_dict[str(origin[index]).lower()][str(desti[index]).lower()] = ori_to_dest[index]
    rw_dict[str(desti[index]).lower()][str(origin[index]).lower()] = dest_to_ori[index]
    return -1
#print (json.dumps 
def fill_unvisited(unvisited):
    for i in range(len(origin)):
        if origin[i] not in unvisited:
            unvisited.append(origin[i])
        if desti[i] not in unvisited:
            unvisited.append(desti[i])

def dijkstra(start):
    heap = []
    visited = []
    unvisited = []
    current = start
    fill_unvisited(unvisited)
    rw_dict[start][start] = 0 #added cost orig -> orig = 0 so prev node cost + node cost works for first pass
    while len(visited) < len(unvisited) - 1:
        if current not in visited:
            visited.append(current)
        for nx_node in rw_dict[current]:
            if nx_node not in visited:
                if (rw_dict[current][nx_node] + rw_dict[start][current], nx_node) not in heap:
                    heapq.heappush(heap, (rw_dict[current][nx_node] + rw_dict[start][current], nx_node)) #node[0] is cost, [1] is station 
        for node in heap:#can probably be optimised by only checking the new nodes added to the heap instead of the whole heap every time, 
            #print (node)
            if node[1] not in rw_dict[start] or (node[0] < rw_dict[start][node[1]]):
                if node[1] in rw_dict[current]:
                    rw_dict[start][node[1]] =  node[0]
        #print("visited", len(visited))
        #print(len(heap))num goes high on oxford very erratic
        if len(heap) > 0:
            c, current =heapq.heappop(heap)
        #print("current", current)
    return -1

def TSP(start, end, middles):
    best_cost = int(99999999999999)
    best_path = []
    printed_path = []
    perms = permutations(middles)
    for perm in perms:
        cost = 0
        for i in range(len(perm) - 1):
            cost += rw_dict[perm[i]][perm[i+1]]
        cost += rw_dict[start][perm[0]] + rw_dict[perm[len(perm) - 1]][end]
        if cost < best_cost:
            best_path.clear()
            best_cost = cost
            best_path.append(start)
            for loca in perm:
                best_path.append(loca)
            best_path.append(end)
    for index, i in enumerate(best_path):
        if index < len(best_path ) - 1:
            printed_path.append(i)
            printed_path.append(" -> ")
        else:
            printed_path.append(i)
    print("best path: ", printed_path)
    print("cost:", best_cost)
    return -1

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
    middle_nodes.append(between)

dijkstra(tv_origin)
for i, mid_stat in enumerate(middle_nodes):
    if mid_stat not in rw_dict[tv_origin]:
        print("middle station ", mid_stat ,  " is not connected to start station, aborting")
        exit()
    else:
        dijkstra(mid_stat)
        middle_dicts.append(rw_dict[mid_stat])
dijkstra(tv_desti)
origin_dict = rw_dict[tv_origin]
desti_dict = rw_dict[tv_desti]

#print(rw_dict[tv_origin])
#print("------------------")
#print(rw_dict[tv_desti])
#print("------------------")
#print(middle_dicts) 

TSP(tv_origin, tv_desti, middle_nodes)