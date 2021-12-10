from struct import *

def compressRLE(file, message):
    encoding = ''
    prev_char = ''
    count = 1

    if not message: return ''

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

        output_file = open("./encoded/"+file.split(".")[0] + ".rle", "wb")
        for data in encoding: # DA stora a um elemento da data
            #cada elemento de um indice do dicionário é little endian ">" e ocupa 2 bytes "H" (ver documentação do pack() ), por isso a MAX_WIDTH NÃO PODE SER MAIOR QUE 16 bits
            output_file.write(pack('>H',int(data))) 
            
        output_file.close()

        return encoding


def decompressRLE(file):
    file = open("./encoded/"+file.split(".")[0]+".rle", "rb")
    compressed_data = []
    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)
    file.close()
    
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(compressed_data) - 1):
        run_count = int(compressed_data[i])
        run_word = compressed_data[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


    # storing the decompressed string into a file.
    output_file = open("./decoded/decodedRLE"+file, "wb")
    output_file.write(bytearray(seq.encode()))
        
    output_file.close()
    return seq


def testeRLE():
    # the original string
    our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA"
    # pass in the original string
    encoded_message = compressRLE(our_message)
    # pass in the decoded string
    decoded_message = decompressRLE(encoded_message)
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message + "]")
    print("Decoded string: [" + decoded_message + "]")
