# https://www.interviewbit.com/courses/programming/topics/trees/problems/bst-iterator/
# 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def last(arr):
    if len(arr) == 0: return None
    return arr[len(arr)-1]

class BSTIterator:
    
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = [root] if root is not None else []
        self.returnedFromStack = {}
        self._refillStack()
        self.lastReturned = -1

    def _refillStack(self):
        while len(self.stack) != 0 and last(self.stack).left is not None:
            self.stack.append(last(self.stack).left)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        if not self.hasNext(): return None
        
        top = last(self.stack)
        self.lastReturned = top.val
        self.returnedFromStack[self.lastReturned] = True
        
        while top is not None and top.val in self.returnedFromStack:
            
            def processRight():
                top = last(self.stack)
                if top is not None \
                    and top.right is not None \
                    and top.val in self.returnedFromStack \
                    and top.right.val > self.lastReturned:
                        self.stack.append(top.right)
                        self._refillStack()
                        return True
                return False
                
            if not processRight():
                self.stack.pop()
                del self.returnedFromStack[top.val]
                processRight()

            top = last(self.stack)
        
        return self.lastReturned

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

