#######################################
# !! DENNE KODEN GIR BARE 64 POENG !! #
#######################################

def main():
    def BFS(adj, src, dest, v, pred, dist):
        queue = []
    
        visited = [False for i in range(v)]
    
        for i in range(v):
            dist[i] = 1000000
            pred[i] = -1

        visited[src] = True
        dist[src] = 0
        queue.append(src)
        while (len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            for i in range(len(adj[u])):
                if (visited[adj[u][i]] == False):
                    visited[adj[u][i]] = True
                    dist[adj[u][i]] = dist[u] + 1
                    pred[adj[u][i]] = u
                    queue.append(adj[u][i])
                    if (adj[u][i] == dest):
                        return True
        return False
    
    def printShortestDistance(adj, s, dest, v):
        pred=[0 for i in range(v)]
        dist=[0 for i in range(v)]
    
        
        if (BFS(adj, s, dest, v, pred, dist) == False):
            print("Given source and destination are not connected")
        

        path = []
        crawl = dest
        path.append(crawl)
        
        while (pred[crawl] != -1):
            path.append(pred[crawl])
            crawl = pred[crawl]

        print(dist[dest]+1)


    adj_list = {}
    mylist = []
    
    def add_edge(node, node1, node2):
        if node not in mylist:
            mylist.append(node)
            
        temp = []
        if node1 not in adj_list:
            temp.append(node2)
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp.append(node2)
            adj_list[node1] = temp


    N = int(input())

    for i in range(N-1):
        e = i+1
        a, b, c = map(int, input().split())
        add_edge(e,e,a)
        add_edge(e,e,b)
        add_edge(e,e,c)
        add_edge(e,e,e+1)

    printShortestDistance(adj_list, 1, N, N*3)

main()