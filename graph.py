import pydot

class GraphViz:
    def __init__(self, data_relations):
        self.subj = data_relations['arg1'].to_list()
        self.obj = data_relations['arg2'].to_list()
        self.rel = data_relations['rel'].to_list()
        self.nodes = []
        self.edges = []
        self.seen = set()
        self.graph = pydot.Dot(graph_type='digraph', rankdir = 'LR')
        self.fill_graph()
    
    def __str__(self):
        return 'Nodes:' + str(self.nodes) + '\n' + 'Edges:' + str(self.edges)
    
    def get_node(self, text):
        if text.lower() in self.seen:
            for node in self.nodes:
                if node.get_attributes()['label'].lower() == text.lower():
                    return node
        node = pydot.Node(text, label = text)
        self.nodes.append(node)
        self.graph.add_node(node)
        self.seen.add(text.lower())
        return node
    
    def add_sub_nodes(self, node, key):
        for i in range(len(DICT_COMM[key])):
            sub_node = self.get_node(DICT_COMM[key][i])
            sub_edge = pydot.Edge(node, sub_node, label = '')
            self.edges.append(sub_edge)
            self.graph.add_edge(sub_edge)
            
    def fill_graph(self):
        for c1, c2, r in zip(self.subj, self.obj, self.rel):
            #print(c1, c2, r)
            node1 = self.get_node(c1)
            # if any(key in c2 for key in DICT_COMM):
            #     for key in DICT_COMM:
            #         if any(value in c2 for value in DICT_COMM[key]):
            #             node2 = self.get_node(key)
            #             self.add_sub_nodes(node2, key)
            # else:
            #     #print('second',c2)
            node2 = self.get_node(c2)
            edge = pydot.Edge(node1, node2, label = ' ' + r)
            self.edges.append(edge)
            self.graph.add_edge(edge)