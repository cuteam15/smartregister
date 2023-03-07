import zbar
import time

# create a Scanner object
scanner = zbar.Scanner()

# open the barcode scanner device
dev = "/dev/input/event0"
barcode = open(dev, "rb")

# start scanning for barcodes
while True:
    # read the barcode data
    data = barcode.read(16)
    barcode.flush()

    # decode the barcode data
    symbols = scanner.scan(data)

    # print the barcode data
    for symbol in symbols:
        print(symbol.data)
        
    # wait for a second before scanning the next barcode
    time.sleep(1)
