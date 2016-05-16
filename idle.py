from treelib import Tree, Node


    
 #---------------------------------------------------------   
def create_tree():
     
     tree = Tree()
     tree.create_node("individual consumption expenditure of households", "00")  # root node
     tree.create_node("food and non-alcoholic beverages", "01", parent="00")
     tree.create_node("food", "01.1", parent="01")
     tree.create_node("non-alcoholic beverages", "01.2", parent="01")
     tree.create_node("alcoholic beverages, tobacco and narcotics", "02", parent="00")
     tree.create_node("alcoholic beverages", "02.1", parent="02")
     return tree
#----------------------------------------------------------
def example(desp):
    sep = "-"*20 + '\n'
    print(sep + desp)

if __name__ == '__main__':
    tree = create_tree()

    example("COICOP Emerging Markets - till Level 6 of granularity")
    tree.show(idhidden=False,key=lambda x: x.tag, reverse=True, line_type='ascii-em')

for node in tree.expand_tree():
    #print(tree[node].tag)
    print(node)

    
