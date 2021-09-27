# basics
for x in range(0,151):
    print(x)
# multiples of five
for x in range(5, 1001, 5):
    print(x)
#counting, the dojo way
for x in range(1,101):
    if (x % 5 == 0 and x % 10 == 0):
        print("Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
# whoa. that sucker's huge
count = 0
for x in range(0, 500000):
    if x % 2 == 1:
        count += x
        print(count)
# countdown by fours
for x in range(2018, 0, -4):
    print(x)
#flexible counter
lowNum = 2
highNum = 8
mult = 2
for mult in range(lowNum, highNum+1):
    if mult % 2 == 0:
        print(mult)