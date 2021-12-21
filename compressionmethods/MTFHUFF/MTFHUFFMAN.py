import compressionmethods.MTF.MoveToFront as MTF
import compressionmethods.HuffmanCODEC.huffmancodec as hf
from compressionmethods.HuffmanCODEC.huffmancodec import *


def encodemtfhuff(file_name, data, alf):
    mtf = MTF.move2front_encode(data, alf)

    codec = HuffmanCodec.from_data(mtf)
    symbols, length = codec.get_code_len()

    codec.save("./compressionmethods/MTFHUFFMAN/" +
               file_name.split(".")[0]+'.LZWhuffTable')

    bytes_encoded = codec.encode(mtf)
    output_file = open("./compressionmethods/MTFHUFFMAN/" +
                       file_name.split(".")[0]+".LZWhuffData", "wb")
    output_file.write(bytes_encoded)
    output_file.close()


def decodemtfhuff(file, alf):
    codec = HuffmanCodec.load(
        "./compressionmethods/MTFHUFFMAN/"+file.split(".")[0]+'.LZWhuffTable')

    data = codec.decode(open("./compressionmethods/MTFHUFFMAN/" +
                             file.split(".")[0]+".LZWhuffData", "rb").read())

    strdecompressed = MTF.move2front_decode(data, alf)
    MTF.writetofileDEC(
        "./compressionmethods/MTFHUFFMAN/decodedMTFHUFF"+file, strdecompressed)
