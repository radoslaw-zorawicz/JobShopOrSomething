class VertexMetadata:
    def __init__(self):
        self.inDegree = 0
        self.longestPath = 0
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return self.__str__()


def evaluate(solution):
    v = [VertexMetadata() for i in range(0, len(solution.directed))]
    __inDegrees(solution, v)
    noInputV = [solution.START]
    while noInputV:
        current = noInputV.pop()
        time = 0
        if current != solution.START and current != solution.END:
            time = solution.problem.operations[current].time
        path = v[current].longestPath + time

        for adj in solution.directed[current]:
            v[adj].inDegree -= 1
            if path > v[adj].longestPath:
                v[adj].longestPath = path
            if v[adj].inDegree == 0:
                noInputV.append(adj)

    if v[solution.END].inDegree != 0:
        print("Cycle detected, current graph is: ")
        print(solution)
        print("Current vertices metadata is: ")
        print(v)
        raise "Suicide"
    return v[solution.END].longestPath

def __inDegrees(solution, v):
    for s in range(0, len(solution.directed)):
        for e in solution.directed[s]:
            v[e].inDegree += 1
