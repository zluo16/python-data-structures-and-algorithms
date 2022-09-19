from graph_node_class import GraphNode


class Solution:
    def cloneGraph(self, node: GraphNode) -> GraphNode:
        clone_hash = {}

        def dfs_mapper(node):
            if node in clone_hash:
                return clone_hash[node]

            cloned = GraphNode(node.val)
            clone_hash[node] = cloned

            for n in node.adjacent:
                cn = dfs_mapper(n)
                cloned.adjacent.append(cn)

            return cloned

        dfs_mapper(node)

        return clone_hash[node]
