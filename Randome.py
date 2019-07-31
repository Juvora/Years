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

# Если у вас разные условия ведут к одному и тому же результату, значит их надо объединить
if (a < b and a > c) or (a >= b and b >= c):
    print(c)
elif a < b and a <= c:
    print(a)
else:
    print(b)
