from graph.graphweighted import *


# """ Graph 1 """
#
# # Small simple graph from JS online session
# v = "ABCD"
# e = ["AB", "AC", "BD"]
# g = Graph(v, e)
# # Test small simple graph from breadth
# # d = g.breadth2()
# # print(d)
#
#
# """ Graph 2 """
#
# # Graph 2 -> From return_rugraph
# v = "ABCDEFG"
# e = ["FA", "EG", "DE", "EF", "FB",
#      "GC", "EA", "AG", "DG"]
# g2 = Graph(v, e)
# # Test graph 2 breadth
# d = g2.breadth()
# # print(d)
#
#
# """ Graph 3 """
# # Create graph vertices and edges
# v = "ABC"
# e = ["AB", "BC", "CA"]
# g3 = Graph(v, e)
# # Display graph data
# nodes_a = list(g3.vertices)
# nodes_a.sort()
# # print(nodes_a)


""" Graph 4 """
# Create Graph
v = "ABCDEFGHI"
e = ["AI91", "GC9", "FG32", "ED47",
     "DF75", "BC72", "IC22", "AF59",
     "IB76"]
g4 = WeightedGraph(v, e)
print("g4.mst()", g4.mst())