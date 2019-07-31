day = int(input())
month = int(input())
year = int(input())


today1 = 25
today2 = 7
today3 = 2019

ok = today3 - year
if today2 < month:
    ok = ok - 1
else:
    if month == today2 and today1 <= day:
        ok = ok - 1

# Чтобы не использовать связку else-if в Python есть elif
if today2 < month:
    ok = ok - 1
elif month == today and today <= day:
    ok = ok - 1
# Также у вас два условия, которые ведут к одному результату, значит их можно объединить
if today2 < month or month == today and today <= day:
    # Можно использовать -= вместо ok = ok - 1
    ok -= 1

print("You age is ", ok)
