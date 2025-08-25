import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
def ma_star(start, goal, neighbors, memory_limit):
    open_set = [(0, start)]  
    came_from = {}
    g_score = {start: 0}
    memory_used = 0

    while open_set:
        _, current = heapq.heappop(open_set)


        print(f"Current node: {current}, Open set size: {len(open_set)}, Memory used: {memory_used}")

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], memory_used

        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

        memory_used = max(memory_used, len(open_set) + len(came_from))
        if memory_used > memory_limit:
            print(f"Exceeded memory limit ({memory_limit} units)")
            return None, memory_used

    return None, memory_used

def neighbors(node):
    x, y = node
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

start = (0, 0)
goal = (5, 5)
memory_limit = 20  

path, memory_used = ma_star(start, goal, neighbors, memory_limit)
if path is not None:
    print(f"Path from {start} to {goal}:")
    for step in path:
        print(step)
    print(f"Memory used: {memory_used} units of memory")
else:
    print(f"No path found from {start} to {goal} within memory limit of {memory_limit} units of memory")
