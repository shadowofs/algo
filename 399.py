from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = {}
        for equation, value in zip(equations, values):
            edges.setdefault(equation[0], {})[equation[1]] = value
            edges.setdefault(equation[1], {})[equation[0]] = 1 / value

        def cal(equation: List[str], visited=None) -> float:
            if visited is None:
                visited = set()
            if equation[0] not in edges or equation[1] not in edges:
                return -1.0

            if equation[0] == equation[1]:
                return 1.0

            for node, value in edges[equation[0]].items():
                if node in visited:
                    continue

                visited.add(node)
                res = cal([node, equation[1]], visited)
                if res == -1.0:
                    continue

                res *= value
                return res

            return -1.0

        result = []
        for q in queries:
            result.append(cal(q))

        return result


if __name__ == "__main__":
    print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))