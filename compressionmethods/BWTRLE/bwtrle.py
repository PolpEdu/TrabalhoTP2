import compressionmethods.BWT.Burrows_Wheeler as BWT
import compressionmethods.RLE.RLE as RLE
blocksize = 100


def writetofile(file, data):
    with open(file, "wb") as f:
        f.write(data)
        f.close()


def bwtrleenc(file, data, BLOCKSIZE):
    bwtenc = BWT.encode(data, BLOCKSIZE)
    bwtrle_encoded = RLE.compressRLE(file, bwtenc)
    RLE.writetofileDEC("./compressionmethods/BWTRLE/" +
                       file.split(".")[0]+".bwtrle", bwtrle_encoded)


def bwtrledec(file):
    bwt_encoded = RLE.readfromfile(
        "./compressionmethods/BWTRLE/"+file.split(".")[0]+".bwtrle")
    decodedRLE = RLE.decompressRLE(bwt_encoded)
    print(decodedRLE)
    bwtdec = BWT.decode(decodedRLE, blocksize)
    print(bwtdec)
    BWT.writetofileDEC(
        "./compressionmethods/BWTRLE/decodedBWTRLE"+file, bwtdec)
