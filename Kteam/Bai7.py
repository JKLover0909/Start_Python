so1 = input("Nhap so 1: ")
so2 = input("Nhap so 2: ")
try:
    SoA = float(so1)
    SoB = int(so2)
    print('{0:.{1}f}'.format(SoA,SoB))
except:
    print("Nhap sai dinh dang")