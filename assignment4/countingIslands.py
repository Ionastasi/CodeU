from disjointset import DisjointSet

def countingIslands(islandsMap):
    """Given a 2-dimensional map of tiles. Each tile is either land or water.
    Counts the number of islands.

    Args:
        islandsMap: a 2-dimensional array of booleans, where False means water
                    and True means land.

    Returns:
        an integer, the number of islands.
    """
    islands = DisjointSet()
    rows = len(islandsMap)
    if rows:
        cols = len(islandsMap[0])
    for x in range(rows):
        for y in range(cols):
            if not islandsMap[x][y]:
                continue
            counter = islands.makeSet()
            islandsMap[x][y] = counter
            # iterate through adjacent cells that we already processed
            for dx, dy in [[-1, 0], [0, -1]]:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_y >= 0 and islandsMap[new_x][new_y]:
                    islands.unionSets(counter, islandsMap[new_x][new_y])
    return islands.getSetCount()
