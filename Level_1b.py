import json
f = open("/content/level1b.json","r")
data = json.load(f)

dic = {}
dic['r0'] = {}
dic['r0']['order_quantity'] = 0
dic['r0']['distances'] = data['restaurants']['r0']['neighbourhood_distance']

for i in data['neighbourhoods'].keys():
    dic[i] = data['neighbourhoods'][i]
count = 1
for i in dic.keys():
    if i!='r0':
      dic[i]['distances'].insert(0,dic['r0']['distances'][count])
      count+= 1
    else:
      dic['r0']['distances'].insert(0,0)
dic_key = [i for i in dic.keys()]
print(len(dic_key))

path = []
keys = [i for i in dic.keys()]
capacity = 0
counter = 0
path.append([])
def travellingsalesman(c):
    global cost
    global capacity
    global counter
    adj_vertex = -1
    visited[c] = 1
    min_val = float('inf')
    path[counter].append(keys[c])
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
          if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if capacity + dic[keys[adj_vertex]]['order_quantity'] > 1120:
        capacity = 0
        path[counter].append(keys[0])
        counter += 1
        path.append([])
        travellingsalesman(0)
    else:
        capacity += dic[keys[adj_vertex]]['order_quantity']
        if (min_val != float('inf')):
          cost = cost + min_val
        if adj_vertex == -1:
          adj_vertex = 0
          path[counter].append(keys[adj_vertex])
          cost = cost + tsp_g[c][adj_vertex]
          return
        travellingsalesman(adj_vertex)

n = len(keys)
cost = 0
visited = [0]*n
tsp_g = []
for i in dic.keys():
    tsp_g.append(dic[i]['distances'])
travellingsalesman(0)

print(path)
print(visited)
output = {}
output['v0'] = {}
counter = 0
for i in range(len(path)):
  output['v0']['path'+str(i)] =path[i]
seet = []



outfile = open('level1b_output.json','w')
json.dump(output,outfile)
outfile.close()