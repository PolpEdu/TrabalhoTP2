import compressionmethods.LZW.LZW as LZW
from compressionmethods.HuffmanCODEC.huffmancodec import *


def lzwHuffmanenc(file_name, data, MAX_WIDTH):
    compressed_data_LZW = LZW.compress(file_name, data, MAX_WIDTH)

    codec = HuffmanCodec.from_data(compressed_data_LZW)
    symbols, length = codec.get_code_len()
    codec.save("./compressionmethods/LZWHUFFMAN/" +
               file_name.split(".")[0]+'.LZWhuffTable')

    bytes_encoded = codec.encode(compressed_data_LZW)

    output_file = open("./compressionmethods/LZWHUFFMAN/" +
                       file_name.split(".")[0]+".LZWhuffData", "wb")
    output_file.write(bytes_encoded)
    output_file.close()


def lzwHuffmandec(file):
    codec = HuffmanCodec.load(
        "./compressionmethods/LZWHUFFMAN/"+file.split(".")[0]+'.LZWhuffTable')

    data = codec.decode(open("./compressionmethods/LZWHUFFMAN/" +
                             file.split(".")[0]+".LZWhuffData", "rb").read())

    strdecompressed = LZW.decompress(data)
    LZW.writeoutputDECtofile(
        "./compressionmethods/LZWHUFFMAN/decodedLZWHUFFMAN"+file, strdecompressed)
