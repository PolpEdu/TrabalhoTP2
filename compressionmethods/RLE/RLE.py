from struct import *


def compressRLE(file, message):
    encoding = ''
    prev_char = ''
    count = 1

    if not message:
        return ''

    for char in message:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char

        return encoding


def writetofileENC(file, encoding):
    output_file = open("./encoded/"+file.split(".")[0] + ".rle", "wb")
    for data in encoding:  # DA stora a um elemento da data
        # cada elemento de um indice do dicionário é little endian ">" e ocupa 2 bytes "H" (ver documentação do pack() ), por isso a MAX_WIDTH NÃO PODE SER MAIOR QUE 16 bits
        output_file.write(pack('>B', ord(data)))

    output_file.close()

    return len(encoding)


def decompressRLE(filename):
    file = open("./encoded/"+filename.split(".")[0]+".rle", "rb")
    compressed_data = []
    # Reading the compressed file.
    while True:
        rec = file.read(1)
        if len(rec) != 1:
            break
        (data, ) = unpack('>B', rec)
        compressed_data.append(data)
    file.close()

    decode = ''
    count = ''
    for char in compressed_data:
        c = chr(char)
        if c.isdigit():
            # ...append it to our count
            count += c
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += c * int(count)
            count = ''

    return decode


def writetofileDEC(filename, decode):
    # storing the decompressed string into a file.
    output_file = open("./decoded/decodedRLE"+filename, "wb")
    output_file.write(bytearray(decode.encode()))

    output_file.close()
    return len(decode)
