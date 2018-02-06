#Project euler problem 40

string = ""
i = 1

while len(string) < 1000000:
    string = string + str(i)
    i += 1

L = list(string)
print(int(L[0])*int(L[9])*int(L[99])*int(L[999])*int(L[9999])*int(L[99999])*int(L[999999]))