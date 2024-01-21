def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(leap_year(2000))
print(leap_year(1900))
print(leap_year(1997))