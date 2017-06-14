def find_simple_path(nodes, edges, length):
    if length == 1:
        return [[node] for node in nodes]
    prev_paths = find_simple_path(nodes, edges, length-1)
    paths = []
    prime_path = []
    for path in prev_paths:
        if len(path)>1 and path[0] == path[-1]:
            continue
        for next_node in edges[path[-1]]:
            if next_node in path[1:-1]:
                continue
            else:
                paths.append(path + [next_node])
    return paths

def A_in_B(A,B):
    if(any([A == B[i:i+len(A)] for i in range(0,len(B)-len(A)+1)])):          
        return True
    return False

def find_prime_path(paths): 
    paths = sorted(paths, key = lambda paths:len(paths))
    prime_path = []
    length = len(paths)
    for i in range(length):
        path = paths[i]
        flag = False
        if len(path)>1 and path[0] == path[-1]:
            prime_path.append(path)
        else:
            for j in range(i+1, length):
                path2 = paths[j]
                if (A_in_B(path,path2)):
                    flag = True
                    break
            if not flag:
                 # print(path)
                prime_path.append(path)
    return prime_path

def process(nodes, edges,i):
    length = len(nodes) + 1
    simple_path = []
    for n in range(length):
        simple_path += find_simple_path(nodes, edges, n+1)

    result = find_prime_path(simple_path)
    result = sorted(result, key = lambda x:(len(x), x[:]))
    total = len(result)

    answer='ans/ans'+str(i)+'.txt'
    ans = open(answer,'w')
    ans.write(str(total)+'\n')
    for res in result:
        ans.write(str(res)+'\n')

def readGraph(fileName):
    graph = []
    with open(fileName,'r') as f:
	f.readline()
        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip('[]\n')
            a = list(line.split(","))
            a = [int(x) for x in a]
            if a[0] == -1:
                a = []
            graph.append(a)
    return graph

if __name__ == '__main__':
    for i in range(16):
            case='case/case'+ str(i) +'.txt'
            edges = readGraph(case)
            nodelen = len(edges)
            nodes = list(range(nodelen))
            process(nodes, edges, i)
            print('case' + str(i) + ' is ok!')
