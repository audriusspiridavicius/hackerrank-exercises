from collections import OrderedDict


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def get_top_view(node:Node, level:int, values:dict, vd = 0):
    
    if node:
        current = node
        if level not in values or (level in values and vd < values[level][1]):
            values[level] = (current.info,vd)
            
        if node.left:
            get_top_view(node.left, level - 1, values, vd+1)
            
        if node.right:
            get_top_view(node.right, level + 1, values, vd+1)
    

def topView(root):
    
    results = OrderedDict()
    
    if root:
        get_top_view(root, 0, results)
    top_view_values = [value[0] for key,value in sorted(results.items(), key= lambda val:val[0])]  
    srtd = map(str,top_view_values)

    print(" ".join(srtd))
    
    


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = 116
    arr = [37, 23, 108, 59, 86, 64, 94, 14, 105, 17, 111, 65, 55, 31, 79, 97, 78, 25, 50, 22, 66, 46, 104, 98, 81, 90, 68, 40, 103, 77, 74, 18, 69, 82, 41, 4, 48, 83, 67, 6, 2, 95, 54, 100, 99, 84, 34, 88, 27, 72, 32, 62, 9, 56, 109, 115, 33, 15, 91, 29, 85, 114, 112, 20, 26, 30, 93, 96, 87, 42, 38, 60, 7, 73, 35, 12, 10, 57, 80, 13, 52, 44, 16, 70, 8, 39, 107, 106, 63, 24, 92, 45, 75, 116, 5, 61, 49, 101, 71, 11, 53, 43, 102, 110, 1, 58, 36, 28, 76, 47, 113, 21, 89, 51, 19, 3]
    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)