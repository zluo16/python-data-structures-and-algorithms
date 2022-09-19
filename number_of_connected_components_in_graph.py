class Graph:

    def __init__(self, v_count=0):
        self.g_map = {}
        self.v_count = v_count

    def number_of_connected_components(self):
        visited = []
        count = 0

        for k in self.g_map.keys():
            if k not in visited:
                self.dfs_util(k, visited)
                count += 1

        return count

    def dfs_util(self, key, visited):
        visited.append(key)
        for k in self.g_map[key]:
            if k not in visited:
                self.dfs_util(k, visited)
