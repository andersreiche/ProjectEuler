#Project euler problem 67 (Note, this code solves both problem 18 and problem 67)
import numpy
import time
start = time.time()

Tree = []
#Read in the tree as rows of strings
with open("p067_triangle.txt", "r") as f:
    content = f.read()

#Transform the rows of strings into a 2d array of integers forming a trangle
for row in content.split('\n'):
    if row != "":
        L = row.split()
        L = [int(i) for i in L]
        Tree.append(L)
            
#Take the larger of two child nodes and add to the parent node. do this untill root is reached. 
#root(Tree[0][0]) now has the value of the max path sum
Layers = len(L)
print(f"The tree has {Layers} layers")

for row in range(0,Layers-1):
    x = (Layers - 2) - row
    for col in range(0, x + 1):
        y = col
        Tree[x][y] = Tree[x][y] + max(Tree[x + 1][y], Tree[x + 1][y + 1])


elapsed = time.time() - start
print(f"result: {Tree[0][0]} found in {elapsed} seconds.")