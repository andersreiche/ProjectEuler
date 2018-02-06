#Project euler problem 31
import time
start = time.time()
p1 = 1
p2 = 2
p5 = 5
p10 = 10
p20 = 20
p50 = 50
p100 = 100

res = 1
for a in range (0,3):
    print (f"a: {a}")
    if a == 2:
        print("Halfway there!")
    for b in range (0,5):
        print (f"b: {b}")
        for c in range (0,11):
            print (f"c: {c}")
            for d in range (0,21):
                for e in range (0,41):
                    for f in range (0,101):
                        for g in range (0,201):
                            if (p1 * g) + (p2 * f) + (p5 * e) + (p10 * d) + (p20 * c) + (p50 * b) + (p100 * a) == 200:
                                res += 1
elapsed = time.time() - start
print(res)
print(f"result: {res} found in {elapsed} seconds.")
