import heapq

def heuristic(node, goal):
    # Manhattan distance
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(start, goal, neighbors):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None

# Example usage
def neighbors(node):
    x, y = node
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

start = (0, 0)
goal = (5, 5)
path = astar(start, goal, neighbors)

if path is not None:
    print(f"Path from {start} to {goal}:\n{path}")
else:
    print(f"No path found from {start} to {goal}")
