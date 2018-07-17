import csv

with open('AQI_20180717092552.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    # min = reader[1][2]
    min = 100
    area = None
    next(f, None)
    for row in reader:
        num = int(row[2])
        # print(type(num))
        # print(type(min))
        if num < min:
            min = int(row[2])
            area = row[1] + row[0]

    print(area, "空氣最好  ", "AQI 是  ", min)