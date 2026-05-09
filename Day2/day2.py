from collections import deque
from typing import *

def printTree(root):
    q = deque([root])
    while True:
        nextQ = deque([])
        while q:
            curr = q.popleft()

            print(f"{curr.letter} ",end="")
            if curr.left:
                print(f"l:{curr.left.letter} ",end="")
                nextQ.append(curr.left)
            if curr.right:
                print(f"r:{curr.right.letter} ",end="")
                nextQ.append(curr.right)
            print()
        if nextQ:
            q = nextQ
        else:
            break
    
def dayTwo():
    class TreeNode:
        def __init__(self,rank,letter,left=None,right=None):
            self.rank = rank
            self.letter = letter
            self.left = left
            self.right = right

    l_root = None
    r_root = None

    def addNode(root,rank,letter):
        curr = root
        while True:
            # add
            if rank < curr.rank:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(rank,letter)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(rank,letter)
                    break
    
    #read
    with open("Day2/2_1.txt") as file:
        for line in file:
            arr = line.strip().split()
            l = arr[2].split('=')[1][1:-1].split(',')
            l_rank,l_letter = int(l[0]),l[1]
            if l_root is None:
                l_root = TreeNode(l_rank,l_letter)
            else:
                addNode(l_root,l_rank,l_letter)

            r = arr[3].split('=')[1][1:-1].split(',')
            r_rank,r_letter = int(r[0]),r[1]
            if r_root is None:
                r_root = TreeNode(r_rank,r_letter)
            else:
                addNode(r_root,r_rank,r_letter)

    # find biggest level
    left_q = deque([l_root])
    right_q = deque([r_root])
    level_size = 0
    fullWord = ""
    while True:
        lWord = ""
        rWord = ""
        curr_level_size = 0
        next_left_q = deque([])
        next_right_q = deque([])
        while left_q or right_q:

            if left_q:
                curr = left_q.popleft()
                curr_level_size += 1
                lWord += curr.letter
                if curr.left:
                    next_left_q.append(curr.left)
                if curr.right:
                    next_left_q.append(curr.right)
            if right_q:
                curr = right_q.popleft()
                curr_level_size += 1
                rWord += curr.letter
                if curr.left:
                    next_right_q.append(curr.left)
                if curr.right:
                    next_right_q.append(curr.right)
        
        if curr_level_size > level_size:
            level_size = curr_level_size
            fullWord = lWord+rWord

        if not next_left_q and not next_right_q:
            break
        else:
            left_q = next_left_q
            right_q = next_right_q
    
    return fullWord

def dayTwo2():
    class TreeNode:
        def __init__(self,id,rank,letter,left=None,right=None):
            self.id = id
            self.rank = rank
            self.letter = letter
            self.left = left
            self.right = right

    l_root = None
    r_root = None

    def addNode(root,id,rank,letter):
        curr = root
        while True:
            # add
            if rank < curr.rank:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(id,rank,letter)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(id,rank,letter)
                    break
    
    def swapNodes(id,l_root,r_root):
        def find(root):
            q = deque([root])
            while q:
                curr = q.popleft()
                if curr.id == id:
                    return curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        l_found = find(l_root)
        r_found = find(r_root)
        l_found.rank,r_found.rank = r_found.rank,l_found.rank
        l_found.letter,r_found.letter = r_found.letter,l_found.letter
    
    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
            arr = line.strip().split()
            if arr[0] == "ADD":
                id = int(arr[1].split('=')[1])
                l = arr[2].split('=')[1][1:-1].split(',')
                l_rank,l_letter = int(l[0]),l[1]
                if l_root is None:
                    l_root = TreeNode(id,l_rank,l_letter)
                else:
                    addNode(l_root,id,l_rank,l_letter)

                r = arr[3].split('=')[1][1:-1].split(',')
                r_rank,r_letter = int(r[0]),r[1]
                if r_root is None:
                    r_root = TreeNode(id,r_rank,r_letter)
                else:
                    addNode(r_root,id,r_rank,r_letter)
            elif arr[0] == "SWAP":
                id = int(arr[1])
                swapNodes(id,l_root,r_root)

    # find biggest level of each tree
    def find_level(root):
        q = deque([root])
        word = ""
        while True:
            currWord = ""
            nextQ = deque([])
            while q:
                curr = q.popleft()
                currWord += curr.letter
                if curr.left:
                    nextQ.append(curr.left)
                if curr.right:
                    nextQ.append(curr.right)
            
            if len(currWord) > len(word):
                word = currWord

            if nextQ:
                q = nextQ
            else:
                break
        return word
    
    return find_level(l_root)+find_level(r_root)

def dayTwo3():
    class TreeNode:
        def __init__(self,id,rank,letter,parent=None,left=None,right=None):
            self.id = id
            self.rank = rank
            self.letter = letter
            self.parent = parent
            self.left = left
            self.right = right

    l_root = None
    r_root = None

    def addNode(root,id,rank,letter):
        curr = root
        while True:
            # add
            if rank < curr.rank:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(id,rank,letter,curr)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(id,rank,letter,curr)
                    break
    
    def swapNodes(id,l_root,r_root):

        def find_all(root):
            res = []
            q = deque([root])
            while q:
                curr = q.popleft()
                if curr.id == id:
                    res.append(curr)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return res

        def replace_child(parent,old_child,new_child):
            if not parent:
                return

            if parent.left == old_child:
                parent.left = new_child
            else:
                parent.right = new_child

        def swap(node1,node2):
            p1 = node1.parent
            p2 = node2.parent

            if p1:
                replace_child(p1,node1,node2)
            if p2:
                replace_child(p2,node2,node1)
            
            node1.parent,node2.parent = p2,p1

        left_nodes = find_all(l_root)
        right_nodes = find_all(r_root)

        all_nodes = left_nodes+right_nodes
        swap(all_nodes[0],all_nodes[1])

        # update roots
        if l_root == all_nodes[0]:
            l_root = all_nodes[1]
        elif l_root == all_nodes[1]:
            l_root = all_nodes[0]

        if r_root == all_nodes[0]:
            r_root = all_nodes[1]
        elif r_root == all_nodes[1]:
            r_root = all_nodes[0]

        return l_root,r_root

    #read
    with open("Day2/2_3.txt") as file:
        for line in file:
            arr = line.strip().split()
            if arr[0] == "ADD":
                id = int(arr[1].split('=')[1])
                l = arr[2].split('=')[1][1:-1].split(',')
                l_rank,l_letter = int(l[0]),l[1]
                if l_root is None:
                    l_root = TreeNode(id,l_rank,l_letter)
                else:
                    addNode(l_root,id,l_rank,l_letter)

                r = arr[3].split('=')[1][1:-1].split(',')
                r_rank,r_letter = int(r[0]),r[1]
                if r_root is None:
                    r_root = TreeNode(id,r_rank,r_letter)
                else:
                    addNode(r_root,id,r_rank,r_letter)
            elif arr[0] == "SWAP":
                id = int(arr[1])
                l_root,r_root = swapNodes(id,l_root,r_root)

    # find biggest level of each tree
    def find_level(root):
        q = deque([root])
        word = ""
        while True:
            currWord = ""
            nextQ = deque([])
            while q:
                curr = q.popleft()
                currWord += curr.letter
                if curr.left:
                    nextQ.append(curr.left)
                if curr.right:
                    nextQ.append(curr.right)
            
            if len(currWord) > len(word):
                word = currWord

            if nextQ:
                q = nextQ
            else:
                break
        return word
    
    return find_level(l_root)+find_level(r_root)

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()