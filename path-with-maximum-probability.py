class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        # Initialize the adjacency list using defaultdict, where each node points to a list of (probability, neighbor) pairs
        adj = defaultdict(list)
        # Populate the adjacency list with the edges and their corresponding success probabilities
        sz = len(edges)
        for i in range(sz):
            u, v, cost = edges[i][0], edges[i][1], succProb[i] # Extract nodes u, v, and the success probability
            adj[u].append((cost, v))  # Add edge from u to v with probability 'cost'
            adj[v].append((cost, u))  # Add edge from v to u with the same probability
        # Initialize the max heap with the start node, using -1.0 because heapq is a min-heap by default
        maxHeap = [(-1.0, start)]
        # Initialize the probability array where Prob[i] holds the max probability to reach node i
        Prob = [0.0] * n
        Prob[start] = 1.0  # Start node has a probability of 1.0 (since we're already there)
        # Dijkstra-like algorithm to find the maximum probability path
        while maxHeap:
            # Pop the node with the highest probability (convert back to positive)
            cost, node = heapq.heappop(maxHeap)
            cost = -cost  # Convert back to positive because we stored it as negative
            # If we reach the end node, return the probability (cost)
            if node == end:
                return cost
            # Explore neighbors of the current node
            for ccost, cnode in adj[node]:
                # Calculate the new probability through the current node
                newcost = ccost * cost
                # If the new probability is higher, update and push to the heap
                if newcost > Prob[cnode]:
                    Prob[cnode] = newcost  # Update the max probability for cnode
                    heapq.heappush(maxHeap, (-newcost, cnode))  # Push negative for max-heap behavior
        # If the end node is not reachable, return 0.0
        return 0.0