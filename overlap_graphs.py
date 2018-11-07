import sys

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """

        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None


# read FASTA file

def read_fasta(filename_as_string):
    """
    open text file with FASTA format
    read it and convert it into string list
    convert the list to dictionary
    >>> read_fasta('sample.txt')
        {'Rosalind_0000':'GTAT....ATGA', ... }
    """
    f = open(filename_as_string, 'r')
    content = [line.strip() for line in f]
    f.close()

    new_content = []
    for line in content:
        if '>Rosalind' in line:
            new_content.append(line.strip('>'))
            new_content.append('')
        else:
            new_content[-1] += line

    dict = {}
    for i in range(len(new_content)-1):
        if i % 2 == 0:
            dict[new_content[i]] = new_content[i+1]

    return dict

# problem solving


def graph_generate(dict, n):
    answer = []
    for key in dict.keys():
        for k, v in dict.items():
            if dict[key][-n:] == v[:n] and dict[key] != dict[k]:
                answer.append((key, k))
    return answer


graph = Graph()
# print answer as required format
fasta = read_fasta('data/overlap_graph.txt')
for tup in graph_generate(fasta, 3):
    if tup[0] != tup[1]:
        graph.add_edge({tup[0], tup[1]})


print(graph.find_path("Rosalind_5028", "Rosalind_3843"))