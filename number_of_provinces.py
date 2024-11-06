from typing import *

# https://leetcode.cn/problems/number-of-provinces/description/
class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.unique_roots = size

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1: int, index2: int) -> None:
        root1 = self.find(index1)
        root2 = self.find(index2)

        if root1 == root2:
            return

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        self.unique_roots -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Assume inputs are always valid and validation logics will be skipped

        num_nodes = len(isConnected)
        province_finder = UnionFind(num_nodes)

        for node_index in range(num_nodes):
            target_nodes = isConnected[node_index]
            # Because node index starts with 0, we can just check the connection from node_index + 1 to the end.
            for target_node_index in range(node_index + 1, num_nodes):
                if target_nodes[
                    target_node_index
                ]:  # There is a connection betwen node_index and target_node_index
                    province_finder.union(node_index, target_node_index)

        return province_finder.unique_roots

    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        num_nodes = len(isConnected)
        num_province = 0
        visited_mem = [False] * num_nodes

        def dfs(index: int):
            if not visited_mem[index]:
                visited_mem[index] = True
                for next_node_index in range(num_nodes):
                    if isConnected[index][next_node_index]:
                        dfs(next_node_index)

        for node_index in range(num_nodes):
            if not visited_mem[node_index]:
                num_province += 1
                dfs(node_index)

        return num_province

    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        num_nodes = len(isConnected)
        num_province = 0
        visited_mem = [False] * num_nodes

        for node_index in range(num_nodes):
            if not visited_mem[node_index]:
                num_province += 1
                current_nodes = [node_index]
                while len(current_nodes):
                    next_search_nodes = []
                    for current_node_index in current_nodes:
                        visited_mem[current_node_index] = True
                        for next_node_index in range(num_nodes):
                            if (
                                not visited_mem[next_node_index]
                                and isConnected[current_node_index][next_node_index]
                            ):
                                next_search_nodes.append(next_node_index)
                    current_nodes = next_search_nodes

        return num_province


isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNumBFS(isConnected))
