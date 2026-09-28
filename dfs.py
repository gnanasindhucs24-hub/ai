from collections import deque

class Node:
    def __init__(self, b, p=None, a="", d=0):
        self.b, self.p, self.a, self.d = b, p, a, d

def get_neighbors(node):
    idx, (r, c) = node.b.index(0), divmod(node.b.index(0), 3)
    for dr, dc, act in [(-1,0,'UP'), (1,0,'DOWN'), (0,-1,'LEFT'), (0,1,'RIGHT')]:
        if 0 <= r+dr < 3 and 0 <= c+dc < 3:
            nb = list(node.b)
            nb[idx], nb[(r+dr)*3 + c+dc] = nb[(r+dr)*3 + c+dc], nb[idx]
            yield Node(tuple(nb), node, act, node.d + 1)

def get_path(n):
    return get_path(n.p) + [(n.a, n.b)] if n.p else []

def solve(start, goal, mode='bfs', max_d=20):
    q, vis = deque([Node(start)]), set()
    while q:
        n = q.popleft() if mode == 'bfs' else q.pop()
        if n.b == goal: return get_path(n)
        if n.b not in vis and (mode == 'bfs' or n.d < max_d):
            vis.add(n.b)
            q.extend([nbr for nbr in get_neighbors(n) if nbr.b not in vis])

if __name__ == "__main__":
    start = (5, 4, 0, 6, 1, 8, 7, 3, 2)
    goal  = (1, 2, 0, 3, 4, 5, 6, 7, 8)
    
    print("BFS Steps:", len(solve(start, goal, 'bfs')))
    print("DFS Steps:", len(solve(start, goal, 'dfs', max_d=25)))
