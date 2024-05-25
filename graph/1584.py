import heapq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        '''
        visit = vertecies in spanning tree
        '''
        rows, cols = len(points), len(points[0])
        size = len(points)
        adjs = []
        visit = set()
        minheap = []
        total_cost = 0
        # making adj list
        def calculate_distance(index):
            #weight ( j)
            start_x, start_y = points[index][0] , points[index][1]
            adj = []
            for i in range(size):
                if i == index:
                    continue
                else:
                    dest_x , dest_y =  points[i][0] , points[i][1]               
                    weight = abs(start_x - dest_x) + abs(start_y - dest_y)
                    adj.append( (i, weight ))

            return adj 

        for i in range(size):
            adjs.append(calculate_distance(i))
        
        visit.add(0)
        print(adjs)
        for dest, weight in adjs[0]:
            heapq.heappush(minheap, [weight, 0 , dest])
        while len(visit) < size:
            [weight , start , dest] = heapq.heappop(minheap)
            if dest in visit:
                continue
            visit.add(dest)
            total_cost += weight
        # The graph is K_n ( n= size)
            for i in range( size - 1  ):
                print(i)
                edge = adjs[dest][i]
                heapq.heappush(minheap, [edge[1], dest, edge[0] ])

        return total_cost

sol = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

sol.minCostConnectPoints(points)

        