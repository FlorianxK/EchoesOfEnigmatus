from collections import deque
from typing import *

class TreeNode:
    def __init__(self,rank,letter,left=None,right=None):
        self.rank = rank
        self.letter = letter
        self.left = left
        self.right = right

def dayTwo():
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

    def printTree(root):
        q = deque([root])
        while True:
            nextQ = deque([])
            while q:
                curr = q.popleft()
                print(f"{curr.letter}: ",end="")
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
    return

def dayTwo3():
    return

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()