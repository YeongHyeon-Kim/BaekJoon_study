import sys
input = sys.stdin.readline

N = int(input())

tree = {}

for i in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left,right]

def preorder(root):
    if root != '.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root !='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def posorder(root):
    if root != '.':
        posorder(tree[root][0])
        posorder(tree[root][1])
        print(root,end='')

preorder('A')
print()
inorder('A')
print()
posorder('A')