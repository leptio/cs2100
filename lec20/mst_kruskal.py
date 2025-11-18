#"greedy algorithm"
#chooses edge with minimum weight and add it to spanning tree until all vertices are connected
#Greedy is not always optimal, but this algo is optimal

#create forest f (a set of trees), where each vertex in the graph is a separate tree

#create a sorted set s containing all the edges in the graph

#while s is nonempty and f is not yet spanning:
#remove the edge with the minimum weight from s
#if the removed edge connects two different trees, then add it to the forest F, combining two trees into a single tree

