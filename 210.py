from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        edges = {}
        for req in prerequisites:
            edges.setdefault(req[0], 0)
            edges[req[0]] += 1

        for i in range(numCourses):
            if i in edges:
                continue

            result.append(i)

        while prerequisites:
            for idx, req in enumerate(prerequisites):
                if req[1] not in edges:
                    prerequisites.pop(idx)
                    if edges[req[0]] == 1:
                        edges.pop(req[0])
                        result.append(req[0])
                    else:
                        edges[req[0]] -= 1
                    break
            else:
                return []

        return result

if __name__ == "__main__":
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))