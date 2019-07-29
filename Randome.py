a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a > c:
        print(c)
    else:
        print(a)
else:
    if b < c:
        print(b)
    else:
        print(c)
