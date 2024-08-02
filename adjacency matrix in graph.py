class Graph:
    def __init__(self, vno):
        self.vertex== vno
        self.adj_matrix[[0]*vno for e in range(vno)]
    def add_edge(self, u, v, weight=1):
        if 0<= u< self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]= weight
            self.adj_matrix[v][u]= weight
    def remove_edge(self, u, v ):
        if 0<= u< self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]= 0
            self.adj_matrix[v][u]= 0
    def has_edge(self, u, v):
        if 0<= u< self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0 
    def print_adj_matrix(self):
        for row_list in self.adf_matrix:
            print(" ".join(map(str, row_list)))
            