# https://www.geeksforgeeks.org/python/visualize-graphs-in-python/
# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import Language 

# Defining a Class
class GraphVisualization:
 
    def __init__(self):
        
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
        
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
        
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.DiGraph(directed=True)
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, arrowsize=20, width=5, font_color="white", font_size=32, node_size=5300)

        plt.show()

if __name__ == "__main__":

    # Driver code
    G = GraphVisualization()
    # G.addEdge(0, 2)
    # G.addEdge(1, 2)
    # G.addEdge(1, 3)
    # G.addEdge(5, 3)
    # G.addEdge(3, 4)
    # G.addEdge(1, 0)
    # G.addEdge(0, 0)
    # G.visualize()
         
#    length_4_words = Language.words_of_len(["a", "b"], ["abc"], 4)
    length_3_words = Language.words_of_len(["a", "b"], [], 4)
    for i in length_3_words:
        G.addEdge(i[:-1], i[1:])
    
    G.visualize()
