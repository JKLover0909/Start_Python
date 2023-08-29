try:
    with open('xinput.txt','r') as fileInp:
        ten = fileInp.readline().rstrip('\n')
        tuoihientai = int(fileInp.readline())
    with open('xoutput.out','w') as fileOut:
        fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}' .format(ten,tuoihientai+20))
except FileNotFoundError:  
    with open('xoutput.out','w') as fileOut:
        fileOut.write('Khong tim thay file xinput.txt')
except ValueError:
    with open('xoutput.out','w') as fileOut:
        fileOut.write('File xinput.txt khong dung dinh dang')              