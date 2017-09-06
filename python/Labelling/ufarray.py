
class UFarray:
    def __init__(self):
        # Array das label -> armazena as equivalencias
        self.P = []
        # set do meu novo label, quando for criado outro
        self.label = 0

    def criaLabel(self):
        r = self.label
        self.label += 1
        self.P.append(r)
        return r    
    # raiz da Union
    def setRoot(self, i, root):
        while self.P[i] < i:
            j = self.P[i]
            self.P[i] = root
            i = j
        self.P[i] = root
    # Localiza o no raiz que contem o no i
    def findRoot(self, i):
        while self.P[i] < i:
            i = self.P[i]
        return i
    
    # Localiza o no raiz que contem o no i
    # comprimo a arvore
    def find(self, i):
        root = self.findRoot(i)
        self.setRoot(i, root)
        return root    
    
    def union(self, i, j):
        if i != j:
            root = self.findRoot(i)
            rootj = self.findRoot(j)
            if root > rootj: root = rootj
            self.setRoot(j, root)
            self.setRoot(i, root)
    
    def flatten(self):
        for i in range(1, len(self.P)):
            self.P[i] = self.P[self.P[i]]
    
    