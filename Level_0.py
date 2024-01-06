import json
f = open("/content/level0.json","r")
data = json.load(f)
dic = {}
dic['r0'] = data['restaurants']['r0']['neighbourhood_distance']
for i in data['neighbourhoods'].keys():
    dic[i] = data['neighbourhoods'][i]['distances']
count = 1
for i in dic.keys():
    if i!='r0':
      dic[i].insert(0,dic['r0'][count])
      count+= 1
    else:
      dic['r0'].insert(0,0)
f = open("/content/level0_output.json","r")
data = json.load(f)    

path = []
keys = [i for i in dic.keys()]
def travellingsalesman(c):
    global cost
    adj_vertex = -1
    visited[c] = 1
    path.append(keys[c])
    min_val = 9999999999
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if (min_val != 9999999999):
      cost = cost + min_val
    if adj_vertex == -1:
        adj_vertex = 0
        path.append(keys[adj_vertex])
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
n = 21
cost = 0
visited = [0]*n
tsp_g = [i for i in dic.values()]
travellingsalesman(0)

output = {}
output['v0'] = {}
output['v0']['path'] = path
outfile = open('level0_output.json','w')
json.dump(output,outfile)
print(cost)
outfile.close()
