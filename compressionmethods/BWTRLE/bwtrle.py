import compressionmethods.BWT.Burrows_Wheeler as BWT
import compressionmethods.RLE.RLE as RLE


def writetofile(file, data):
    with open(file, "wb") as f:
        f.write(data)
        f.close()


def bwtrleenc(file, data, BLOCKSIZE):
    bwtenc = BWT.encode(file, data, BLOCKSIZE)
    RLE.compressRLE(file, bwtenc)


def bwtrledec(file):
    filesize = BWT.decode(file, BLOCKSIZE)
