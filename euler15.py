#Project euler problem 15
# 40 steps has to be taken, 20 of them must be down and 20 must be right
# The problem can be thought of as "how many permutations are possible of a string with 20 R's and 20 D's"

import math
import time
start = time.time()

# no. of distinct permutations will be n!/(c1!*c2*..*cn!) here n is length of the string
# ck denotes the no. of occurence of each distinct character.
# For eg: string :aabb n=4 ca=2,cb=2
# solution=4!/(2!*2!)=6

permutations = math.factorial(40)/(math.factorial(20) * math.factorial(20))

elapsed = time.time() - start
print(f"result: {permutations} found in {elapsed} seconds.")