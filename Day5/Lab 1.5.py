import glob

L = glob.glob('C:\\Users\\ev.golubyatnik\\Downloads\\config_files\\config_files\\*.txt')
ip = 'ip address'
for name in L:
    with open(name) as f:
        for L in f:
            if ip in L:
                print(L)

