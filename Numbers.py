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


print("You age is ", ok)