import compressionmethods.MTF.MoveToFront as MTF


def encodemtfhuff(file, data, blocksize, alf):
    mtf = MTF.move2front_encode(data, data, alf)
    MTF.writetofile("./compressionmethods/MTFHUFF/" +
                    file.split(".")[0]+".mtf", mtf)
    return len(mtf)


def decodemtfhuff(file):
    pass
