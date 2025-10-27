from collections import deque
def bfs_overall(adj):
    V = len(adj)
    res=[]
    
    visited = [False]*V
    
    for i in range(V):
        if not visited[i]:
            bfs(adj, i, visited, res)
    return res

def bfs(adj,s,visited,res):
    q=deque()
    q.append(s)
    visited[s]= True
    
    while q:
        temp = q.popleft()
        res.append(temp)
        for x in adj[temp]: #for x in range(len(adj[temp]))
            if not visited[x]: #if not visited[adj[temp][x]]
                q.append(x)
                visited[x]= True
            
    return res

# adj=[[1,2],[0,3],[0,4],[1,4],[2,3]]
adj = [[1, 2], [0], [0],[4], [3, 5], [4]]
ans = bfs_overall(adj)
print(ans)

# a=[1,2,3,6]
# for i in range(len(a)):
#     print(a[i])



 #adj list for graph 
# def add_edge(adj,e1,e2):
#     adj[e1].append(e2)
#     adj[e2].append(e1) #undirected

# def display(adj):
#     for i in range(len(adj)):
#         print(f"{i}:",end=" ")
#         for j in adj[i]:
#             print(j,end=" ")
#         print()

# V=4
# adj=[[] for _ in range(V)]

# add_edge(adj,0,1)
# add_edge(adj,0,2)
# add_edge(adj,1,2)
# add_edge(adj,2,3)

# print("dispalying the list")
# display(adj)

# #adj matrix for graph
# def add_edge(mat,e1,e2):
#     mat[e1][e2]=1
#     mat[e2][e1]=1
# def display(mat):
#     for row in mat:
#         print(" ", row)
#         #print(" ".join(map(str, row)))  
# V =4
# mat=[[0]*V for _ in range(V)]
# add_edge(mat,0,1)
# add_edge(mat,0,2)
# add_edge(mat,1,2)
# add_edge(mat,2,3)

# print("display matrix")
# display(mat)

#adj list for bfs for disconnected graph

# from collections import deque

# def bfs(adj,s, visited, res):
    
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr = q.popleft()
#         res.append(curr)
        
#         for i in adj[curr]:
#             if not visited[i]:
#                 visited[i]= True
#                 q.append(i)
#     return res

# def bfs_disconnected(adj):
    
#     res = []
    
#     visited = [False]* len(adj)
    
#     for i in range(len(adj)):
#         if not visited[i]:
#             bfs(adj,i,visited,res)
#     return res
        
# adj = [[1, 2], [0], [0],[4], [3, 5], [4]]
# ans = bfs_disconnected(adj)
# for i in ans:
#     print(i, end=" ")

#adj matrix for disconnected graph bfs
from collections import deque

# Unified BFS function that handles connected and disconnected graphs
def bfs(matrix):
    V = len(matrix)
    visited = [False] * V
    res = []

    for s in range(V):
        if not visited[s]:
            q = deque()
            q.append(s)
            visited[s] = True

            while q:
                curr = q.popleft()
                res.append(curr)

                for i in range(V):
                    if matrix[curr][i] == 1 and not visited[i]:
                        visited[i] = True
                        q.append(i)

    return res

# Function to add undirected edge
def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

# Function to display the matrix
def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

# Main
if __name__ == "__main__":
    V = 6
    matrix = [[0]*V for _ in range(V)]

    # Component 1
    add_edge(matrix, 0, 1)
    add_edge(matrix, 1, 2)

    # Component 2
    add_edge(matrix, 3, 4)

    # Component 3 (node 5 is isolated)

    print("Adjacency Matrix:")
    display_matrix(matrix)

    print("\nBFS Traversal (Handles Disconnected):")
    result = bfs(matrix)
    print(" ".join(map(str, result)))

    
    
    
    
    
    
    
    
       


    
    
    
    
    