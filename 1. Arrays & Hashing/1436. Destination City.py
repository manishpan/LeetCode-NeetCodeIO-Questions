# Problem Statement: You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution:
    def destCity(self, paths):
    # A destination city will not occur in cityA(that is at index 0). So, we first add all the city that are present in index 0 to a set and then we check for city that is not present in that set.
        destination = set()
        for x in paths:
            destination.add(x[0])

        for path in paths:
            if path[1] not in destination:
                return path[1]
            
# Test Cases:
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution().destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().destCity(paths))