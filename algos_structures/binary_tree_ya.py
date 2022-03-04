# while flooding !next free! node in existing tree-structure
def newnode(memstruct):
    memory, firstfree = memstruct
    
    # get next empty node pointer from fillable and make it next empty
    memstruct[1] = memory[firstfree][1]
    return firstfree

# while releasing node, it shifts to first index and becomes the first free node
def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index

# mem manager, left_child of the tree refers to next free cell( /child)
def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i+1, 0])      # [X - key; Y - left_child; Z - right_child]
    return [memory, 0]              # [X - node, Y - pointer to first element]

# search for node in binary tree (key -> value in node; 
# root -> pointer to node with key)
def find(memstruct, root, x):
    key = memstruct[0][root][0]
    
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1       # if nothing found
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)

# f_add + f_createandfillnode implements addition value to the tree
def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]

    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            # if nothing found - add value
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            return add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            # if nothing found - add value
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            return add(memstruct, right, x)

def delete(memstruct, root, y):
    # for "leaf" node with no child nodes (without structure with pointer to parent node)
    index = find(memstruct, root, y)
    if memstruct[0][index][1] == -1 and memstruct[0][index][2] == -1:
        delnode(memstruct, index)
        return

memstruct = initmemory(20)
root = createandfillnode(memstruct, 8)      # filling root node of the tree
add(memstruct, root, 10)
add(memstruct, root, 9)
add(memstruct, root, 14)
add(memstruct, root, 13)
add(memstruct, root, 3)
add(memstruct, root, 1)
add(memstruct, root, 6)
add(memstruct, root, 4)
add(memstruct, root, 7)

delete(memstruct, root, 1)