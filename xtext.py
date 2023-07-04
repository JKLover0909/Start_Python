so2 = 0
so3 = 0
so4 = 0
so1 = int(input("nhap so nguyen: "))
day1 = (input("nhap day so: "))
day = map(int,day1.split())
for x in day:
    if x %2 == 1:
        so2 = so2 + 1
        so4 = so4 + x
    else:
        so3 = so3 + 1
print("so so le la: ", so2)
print("so so chan la: ", so3)
print("tong so le la: ", so4)               