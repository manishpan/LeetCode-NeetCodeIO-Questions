# Problem Statement: Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

#Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = set()
        x, y = 0 ,0
        paths.add((x, y))

        for i in path:
            if i == 'N':    y += 1
            elif i == 'S':  y -= 1
            elif i == 'E':  x += 1
            else:   x -= 1
            if (x, y) in paths:
                return True
            paths.add((x, y))
        
        return False

# Test cases:
path = "NES"
print(Solution().isPathCrossing(path))

path = "NESWW"
print(Solution().isPathCrossing(path))