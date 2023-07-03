daygiatri = input("nhap day so cach nhau boi dau cach: ")
danhsachgiatri = daygiatri.split()
try:
    danhsachso = map(int,danhsachgiatri)
    tong = sum(danhsachso)
    print("tong day so vua nhap la: ", tong)
except:
    print("dinh dang khong hop le")