# import sys
# input=sys.stdin.readline

# root_root = int(input())
# root = root_root
# tree = {root_root : []}
# count = 0
# while count <= 9999:
#     try:
#         temp = int(input())
#     except:
#         break

#     if temp < root_root:
#         if temp < root:
#             tree[root] = [temp, 0]
#         elif temp > root:
#             tree[root] = [0, temp]
#         root = temp
#     else:

#     tree[root] = []

#     count += 1
# print(tree)
# def posorder(root):
#     if root != '.':
#         posorder(tree[root][0])
#         posorder(tree[root][1])
#         print(root,end='')