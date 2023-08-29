so2 = input()
giatri  = False
try:
    so1 = int(so2)
    giatri = True
except:
    print("dinh dang khong hop le")

if giatri == True:
    print("Số thập phân %d trong hệ bát phân là là số: %o" % (int(so1), int(so1)))    