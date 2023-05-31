class Graph:
    def __init__(self,Nodes):
        self.nodes=nodes
        self.adj_list={}
        
        for i in self.nodes:
            self.adj_list[i]=[]
        
    def add_edges(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def print_adj_list(self):
        for i in self.nodes:
            print(i,"-> ",self.adj_list[i])
            
    def degree(self,node):
        deg=len(self.adj_list[node])
        print(deg)

nodes=["A","B","C","D","E"]
g=Graph(nodes)
all_edges=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]
for u,v in all_edges:
    g.add_edges(u,v)

g.print_adj_list()
g.degree("D")










