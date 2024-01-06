import json
f = open("/content/level2b.json","r")
data = json.load(f)

dic = {}
dic['r0'] = {}
dic['r0']['order_quantity'] = 0
dic['r0']['distances'] = data['restaurants']['r0']['neighbourhood_distance']

riders = {}
for i in data['vehicles'].keys():
    riders[i] = data['vehicles'][i]['capacity']
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

path = []
keys = [i for i in dic.keys()]
capacity = 0
counter = 0
path = {}
path['v'+str(0)] = [[]]
for i in range(1,len(riders)):
  path['v'+str(i)] = []

def travellingsalesman(c):
    global cost
    global capacity
    global counter
    adj_vertex = -1
    visited[c] = 1
    min_val = float('inf')
    path['v'+str(counter)][-1].append(keys[c])
    for k in range(n):
        if (visited[k] == 0):
          if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if capacity + dic[keys[adj_vertex]]['order_quantity'] > riders['v'+str(counter)]:
        capacity = 0
        path['v'+str(counter)][-1].append(keys[0])
        counter = (counter+1)%(len(riders))
        path['v'+str(counter)].append([])
        travellingsalesman(0)
    else:
        capacity += dic[keys[adj_vertex]]['order_quantity']
        if (min_val != float('inf')):
          cost = cost + min_val
        if adj_vertex == -1:
          adj_vertex = 0
          path['v'+str(counter)][-1].append(keys[adj_vertex])
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

output = {}
for i in path.keys():
  output[i] = {}
  for j in range(len(path[i])):
    output[i]['path'+str(j+1)] = path[i][j]
    count+= 1
counter = 0
outfile = open('level2b_output.json','w')
json.dump(output,outfile)
outfile.close()