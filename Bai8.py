daygiatri = input("nhap day so cach nhau boi dau cach: ")
danhsachgiatri = daygiatri.split()
tong = 0
danhsachso = map(int,danhsachgiatri)
tong = sum(danhsachso)
print("tong day so vua nhap la: ", tong)