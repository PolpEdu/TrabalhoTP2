
def decode(file, BLOCKSIZE):
    with open(file, "r"):
        for i in range(0, len(texto), BLOCKSIZE):
            bwttry = bwt_tranf(texto[i-BLOCKSIZE:i])
