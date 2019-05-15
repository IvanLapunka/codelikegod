class Solution:

    def wideSearch(self, routes, S, T):
        distance = 1
        last = -1
        queueVertex = [S]
        queued = [0]*1000001
        walked = [0]*1000001
        while len(queueVertex) > 0:
            nextStop = queueVertex.pop(0)
            if nextStop == last:
                last = -1
            walked[nextStop] = 1
            for route in self.stops[nextStop]:
                for stop in routes[route]:
                    if walked[stop] == 0 and queued[stop] == 0:
                        if stop == T:
                            return distance
                        queueVertex.append(stop)
                        queued[stop] = 1
            if last == -1 and len(queueVertex) > 0:
                last = queueVertex[-1]
                distance += 1
        return -1

    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        self.stops = dict()
        for route in range(len(routes)):
            for stop in routes[route]:
                if stop not in self.stops.keys():
                    self.stops[stop] = set()
                self.stops[stop].add(route)
        return self.wideSearch(routes, S, T)






s = Solution()
routes4 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
S = 15
T = 12

print(s.numBusesToDestination(routes4, S, T))

