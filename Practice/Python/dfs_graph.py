from collections import defaultdict


def dfs(adj):
    V = len(adj)
    visited = [False]*V 
    res=[]
    
    for i in range(V):
        if not visited[i]:
            dfs_rec(adj, visited, i, res)
    return res


def dfs_rec(adj,visited,s, res):
    visited[s]=True
    res.append(s)
    
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i, res)
            
adj = [[1, 2], [0], [0],[4], [3, 5], [4]]
ans = dfs(adj)
print(ans)

