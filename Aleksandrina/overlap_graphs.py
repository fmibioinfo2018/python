import queue 
  
class Graph(object):
    def __init__(self, graph_dict=None):
        """if not dictionary is given an empty dictionary will be used"""
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def __str__(self):
        return str(self.__graph_dict).replace('],', '],\n')

    def add_vertex(self, vertex):
        """If vertex is not in graph, vertex will be add to graph with empty list"""
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        (start, end) = tuple(edge)
        if start in self.__graph_dict:
            self.__graph_dict[start].append(end)
        else:
            self.__graph_dict[start] = [end]

    def find_path(self, start, end, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start]
        if start == end:
            return [end]
        if start not in graph:
            return None

        extended_path = None
        for vertex in graph[start]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end, path)
            if extended_path:
                return [start] + extended_path
            
        return None

    def find_path_bfs(self, start, end):
        graph = self.__graph_dict
        parents = {}
        used = [start]
        q = queue.Queue(maxsize=0)
        found = False
        q.put(start)
        while not q.empty() and not found:
            current = q.get()
            if current in graph:
                for vertex in graph[current]:
                    if vertex not in used:
                        used.append(vertex)
                        q.put(vertex)
                        parents[vertex] = current
                        if vertex == end:
                            found = True
                            break

        if not found:
            return None
        current = end
        path = [end]
        while current in parents:
            current = parents[current]
            path = [current] + path

        return path


def read_fasta(file):
    """Open fasta file,read and convert to string list"""
    f = open(file, 'r')
    content = [line.strip() for line in f]
    new_content = {}
    last = ''
    for line in content:
        if ">" in line:
            #new_content.append(line.strip('>'))
            last = line.strip('>')
            new_content[last] = ""
        else:
            new_content[last] += line

    f.close()
    return new_content

def graph_generate(dict, n):
    answer = []
    for key in dict.keys():
        for k,v in dict.items():
            if dict[key][-n:] == v[:n] and key != k:
                answer.append((key, k))

    return answer


def main():
    seq = read_fasta("data/overlap_graph.txt")
    ans = graph_generate(seq, 3)
    graph = Graph()
    for tup in ans:
        if tup[0] != tup[1]:
            graph.add_edge(tup)

    print(graph)
    print(graph.find_path("Rosalind_3725", "Rosalind_6443", []))
    print(graph.find_path_bfs("Rosalind_3725", "Rosalind_6443"))
    print(graph.find_path("Rosalind_7401", "Rosalind_6443", []))
    print(graph.find_path_bfs("Rosalind_7401", "Rosalind_6443"))
    print(graph.find_path("Rosalind_9512", "Rosalind_7282", []))
    print(graph.find_path_bfs("Rosalind_9512", "Rosalind_7282"))
    #print(ans)


if __name__ == "__main__":
    main()