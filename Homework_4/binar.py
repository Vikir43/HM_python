# создание нодов, создание бинарного дерева, добавление значения, удаление значения

class Node:
    def __init__(self, value, left = None, rigth = None):
        self.value = value
        self.left = left
        self.right = rigth
    
    def __str__(self):
        res = f'значение нашего узла: {self.value}'        
        if self.left:
            res += f'значение левого: {self.left.value}'
        if  self.right: 
            res += f' значение правого: {self.right.value}'
        return res
    
        
    #def __del__(self):   # деструктор
        #print("удален узел",self.value)
    
class Tree:
    def __init__(self, root = None):
        self.root = root

    def search(self, node, data, parent = None):
    
        if node == None or data == node.value:    
            return node, parent
        
        if data > node.value:
            return self.search(node.right, data, node)
        if data < node.value:
            return self.search(node.left, data, node)
    
    # если добавляемое значение меньше значения в родительском узле, то новая вершина добавляет в левую ветвь, иначе в правую.
    # если добавленное значение уже присутсвует в дереве, то оно игнорируется.
    def add_node(self, value):
        res = self.search(self.root, value)
        if not res[0]:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print('Ой все, такое значение есть')

    # def delete_node(self, value):
        
    

            
initial_node = Node(15)

tree_1 = Tree(initial_node)
tree_1.add_node(16)
tree_1.add_node(10)

#print(initial_node)

#print(tree_1.search(initial_node, 16))


#print(initial_node)
#tree_1.add_node(16)