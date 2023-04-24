import networkx as nx 
import matplotlib.pyplot as plt
from anytree import Node

array=[]
nodosB=[]
nodosI=[]
nodos0=[]
nodosF=[]
nodosX=[]


def dibujarArbol(nodo: Node):
    array = []
    G = nx.DiGraph()
    array = getArbol(nodo)
    G.add_edges_from(array)
    pos = hierarchy_pos(G)
    nx.draw_networkx_nodes(G,pos, node_size = 500)

    # nodes
    options = {"edgecolors": "tab:gray", "node_size": 500, "alpha": 0.9, "margins" : 0}
    nx.draw_networkx_nodes(G, pos, nodelist=nodosB, node_color="tab:olive", **options)
    nx.draw_networkx_nodes(G, pos, nodelist=nodos0, node_color="tab:blue", **options)
    nx.draw_networkx_nodes(G, pos, nodelist=nodosX, node_color="tab:red", **options)
    nx.draw_networkx_nodes(G, pos, nodelist=nodosI, node_color="tab:purple", **options)
    nx.draw_networkx_nodes(G, pos, nodelist=nodosF, node_color="tab:purple", **options)

    nx.draw_networkx_edges(G,pos, edgelist= G.edges(), edge_color = 'black')
    nx.draw_networkx_labels(G,pos)
    
    plt.show()

def getArbol (nodo: Node):
    pre = str(nodo.id) + nodo.name 
    if(nodo.est == 'B'):
        nodosB.append(pre)
    if(nodo.est == 'I'):
        nodosI.append(pre)
    if(nodo.est == '0'):
        nodos0.append(pre)
    if(nodo.est == 'F'):
        nodosF.append(pre)
    if(nodo.est == 'X'):
        nodosX.append(pre)
    for child in nodo.children:
        getArbol(child)
        pos = str(child.id) + child.name
        array.append((pre,pos))
        print((pre,pos))
    return array

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


    