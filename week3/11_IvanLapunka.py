class Solution:
    '''
    815. Bus Routes, https://leetcode.com/problems/bus-routes/
    We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
    For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in
    the sequence 1->5->7->1->5->7->1->... forever.

    We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
    Travelling by buses only, what is the least number of buses we must take to reach
    our destination? Return -1 if it is not possible.
    '''
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

