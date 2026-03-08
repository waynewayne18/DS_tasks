import sys
from collections import defaultdict
import pandas as pd


rails = pd.read_csv("activity1_3_railnetwork_data.csv", header = None)

tv_middle = []
origin = rails.iloc[:, 0]
desti = rails.iloc[:, 1]
ori_to_dest = rails.iloc[:, 2]
dest_to_ori = rails.iloc[:, 3]

satisfied = 0
found = 0
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

rw_dict = defaultdict(dict)
rw_vertices = [sys.maxsize] * len(origin)

def addNodes(rw_dict, rw_vertices, index):
    rw_dict[origin.iloc[index]][desti.iloc[index]] = ori_to_dest
    rw_dict[desti.iloc[index]][origin.iloc[index]] = dest_to_ori

    return 0

for i in range(len(origin)):
    addNodes(rw_dict, rw_vertices, i)

def dijkstra(start,end):

    return 0

