from anytree import Node, RenderTree, findall_by_attr

a = Node("a")
b = Node("b")
b.parent = a
bb = Node("b")
bb.parent = b
c = Node("c")
c.parent = a

if len(findall_by_attr(a, "c", name = 'name')) == 0:
    print("No existe ningun C")
else:
    print("Existe al menos un C")