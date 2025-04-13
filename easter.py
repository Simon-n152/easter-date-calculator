while True:
    print("Date of Catholic and Orthodox Easter (Gregorian calendar)")
    year = int(input("Enter a year between 1500 and 3000: "))

    from math import trunc
    # Algorithm for calculating Catholic Easter
    a1 = year % 19
    b1 = trunc(year / 100)
    c1 = year % 100
    d1 = trunc(b1 / 4)
    e1 = b1 % 4
    f1 = trunc((b1 + 8) / 25)
    g1 = trunc((b1 - f1 + 1) / 3)
    h1 = (19 * a1 + b1 - d1 - g1 + 15) % 30
    i1 = trunc(c1 / 4)
    k1 = c1 % 4
    l1 = (32 + 2 * e1 + 2 * i1 - h1 - k1) % 7
    m1 = trunc((a1 + 11 * h1 + 22 * l1) / 451)
    p1 = (h1 + l1 - 7 * m1 + 114) % 31
    day1 = p1 + 1
    month1 = trunc((h1 + l1 - 7 * m1 + 114) / 31)
    print(f'\nCatholic Easter: {month1}.{day1}')

    # Algorithm for calculating Orthodox Easter
    a = year % 4
    b = year % 7
    c = year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    # Month and day according to the Julian calendar
    month = trunc((d + e + 114) / 31)
    day = ((d + e + 114) % 31) + 1

    # Conversion to the Gregorian calendar
    if year in range(1500, 1701): day2 = day + 10
    if year in range(1701, 1801): day2 = day + 11
    if year in range(1801, 1901): day2 = day + 12
    if year in range(1901, 2101): day2 = day + 13
    if year in range(2101, 2201): day2 = day + 14
    if year in range(2201, 2301): day2 = day + 15
    if year in range(2301, 2501): day2 = day + 16
    if year in range(2501, 2601): day2 = day + 17
    if year in range(2601, 2701): day2 = day + 18
    if year in range(2701, 2801): day2 = day + 19
    if year in range(2801, 2901): day2 = day + 20
    if year in range(2901, 3001): day2 = day + 21

    # Avoid dates like March 35 or April 37
    if month == 3 and day2 > 31:
        print(f'Orthodox Easter: {month + 1}.{day2 - 31} ({month}.{day})\n')
    elif month == 4 and day2 > 30:
        print(f'Orthodox Easter: {month + 1}.{day2 - 30} ({month}.{day})\n')
    else:
        print(f'Orthodox Easter: {month}.{day2} ({month}.{day})\n')
