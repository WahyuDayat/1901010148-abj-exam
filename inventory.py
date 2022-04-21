file = open ("db-inventory.txt","a")
while True:
    tidak = input ("input data inventory baru ? (ya/tidak)")
    if tidak == 'tidak' or tidak == 'tidak' :
        file = open ("db-inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        break
    elif tidak == 'ya' or tidak == 'ya':
        print("............................")
        x = input ("masukan nama perangkat : ")
        y = input ("masukan lokasi : ")
        file.write("nama perangkat : " +x + ", lokasi : " + y +"\n")
        print("............................")

file.close()