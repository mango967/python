fh=open('mbox-short.txt')
for lx in fh:
    ly=fh.read()
    print(ly.rstrip().upper())

