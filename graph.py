class vertex:
    # Vertex creates the class for the vertex
    # Currently handles all properties of the vertex
    def __init__(self,key):
        self.id = key
        self.label = None
        self.attribute= None
        self.category = []
        self.neighbor = {}
        self.index = {}
        self.searched = False

    # The label for the vertex
    def addlabel(self,label):
        self.label = label
        return

    # The attributes for the vertex
    def addattribute(self,attribute):
        self.attribute = attribute
        return

    # The category for the vertex
    def addcategory(self,category):
        self.category = category
        return

    # The neigbors to the current vertex
    def addneighbor(self,neighbor,path,relationtype):
        relation = {}
        relation['key'] = neighbor
        relation['path'] = path
        relation['relation type'] = relationtype
        self.neighbor[neighbor] = relation

    # The index the vertex belongs to
    def addindex(self,indexName, indexCategory):
        index = {}

        index['name'] = indexName
        index['category'] = indexCategory

        self.index = index

class vertexNode:
    def __init__(self,vertexId):
        self.vertexKey = vertexId
        self.vertexLeft = None
        self.vertexRight = None

class index:
    def __init__(self,indexId,indexName,indexCategory,graphName):
        self.indexId = indexId
        self.indexName = indexName
        self.indexCategory = indexCategory
        self.graphName = graphName
        self.vertex = []

    def searchLeftIndex(self,vertexKey):
        for vert in vertex:
            if vert.vertexKey < vertexKey:
                if vert.vertexRight == None:
                    return vert.vertexKey

    def addVertex(self,vertexKey):
        newVertex = vertexNode(vertexKey)
        self.vertex.append(newVertex)


class graph:
    def __init__(self,graphName):
        self.graphName = graphName
        self.vertex = {}
        self.path = {}
        self.index = {}
        self.MaxVertexKey = 0
        self.MaxIndexId = 0

    def addVertex(self,vertexName,vertexCategory,vertexNeighborKey,vertexNeighborPath,vertexNeighborRelationType,vertexLabel,vertexAttribute):
        self.MaxVertexKey += 1
        newVertex = vertex(self.MaxVertexKey)
        newVertex.addlabel(vertexLabel)
        newVertex.addattribute(vertexAttribute)
        newVertex.addcategory(vertexCategory)
        newVertex.addneighbor(vertexNeighborKey,vertexNeighborPath,vertexNeighborRelationType)
        return self.MaxVertexKey

    def CreateIndex(self,indexName,indexCategory):
        if index[indexName] != None:
            return -1
        self.MaxIndexId += 1
        newIndex = index(self.MaxIndexId,indexName,indexCategory,self.graphName)
        return self.MaxIndexId

    def addIndexVertex(self,indexId,VertexId):
        
