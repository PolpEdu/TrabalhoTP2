# Apply burrows Wheeler Encoding
# def BWTencode(filename, data):

def encode(fich, data, blocksize):
    print("BTW + RLE compression")
    with open("./decoded/decodedBWT"+fich, "w") as f:
        f.close
    for i in range(0, len(data), blocksize):  # divisão em Blocos
        bwttry = bwt_tranf(data[i-blocksize:i])
        with open(write, "a+") as f:
            for n in bwttry:
                f.write(str(n))

    print("racio: {} (read/write)".format(os.stat(fich).st_size/os.stat(write).st_size))
    print("\n")
    return os.stat(fich).st_size/os.stat(write).st_size, end-start


def bwt_tranf(d):
    Input = d
    assert "£" not in Input                     # Input string cannot contain £
    Input = Input + "£"                         # Add "£" to the end of the string
    table = [Input[i:] + Input[:i]
             for i in range(len(Input))]  # Table of rotations of string

    table = sorted(table)

    last_column = [row[-1:]
                   for row in table]             # Last characters of each row
    bwt = ''.join(last_column)
    return bwt


def decode(fich):
    table = [""] * len(bwt)  # Make empty table

    for i in range(len(bwt)):
        table = [bwt[i] + table[i]
                 for i in range(len(bwt))]  # Add a column of r
        print('unsorted = ', table)
        table = sorted(table)
        print('sorted    =', table)

        inverse_bwt = [row for row in table if row.endswith(
            "£")][0]  # Find the correct row (ending in £)

        # Get rid of start and end markers
        inverse_bwt = inverse_bwt.rstrip("£")

        print(inverse_bwt)


'''
    to_encode = "".join(last_column)
    output_file = open("./encoded/"+filename.split(".")[0]+".bwt", "wb")
    # escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(to_encode.encode()))
    output_file.close()
'''

'''
    output_file = open("./decoded/decodedBWT"+filename, "wb")
    # escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(stringfinal.encode()))
    output_file.close()
'''
