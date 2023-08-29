with open('xinput.txt','r') as fileInp:
    fullfile = fileInp.read()
    xephang = fullfile.split()
    fullcau = ' '.join(xephang)
with open('xoutput.out','w') as fileOut:
    fileOut.write(fullcau)    