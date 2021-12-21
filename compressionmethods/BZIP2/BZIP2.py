import bz2
compressionLevel = 9


def writetofile(destination_file, data):
    fh = open(destination_file, "wb")
    fh.write(data)
    fh.close()


def writetofileENC(destination_file, data):
    fh = open(destination_file, "wb")
    fh.write(data)
    fh.close()


def compress(data):
    return bz2.compress(data, compressionLevel)


def decompress(data):
    return bz2.decompress(data)
