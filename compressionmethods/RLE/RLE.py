from struct import *


def compressRLE(filename, data):

    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
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

        output_file = open("./encoded/"+filename.split(".")[0]+".rle", "wb")
        output_file.write(bytearray(encoding.encode()))
        output_file.close()
        return encoding


def decompressRLE(filename):
    input_file = open("./encoded/"+filename.split(".")[0] + ".rle", "rb")
    sequence = []
    while True:
        data = input_file.read(2)
        if not data:
            break
        sequence.append(unpack('>H', data)[0])
    print(sequence)
    decoded_message = "".join(sequence)
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2

    output_file = open("./decoded/decodedRLE"+filename, "wb")
    output_file.write(bytearray(stringfinal.encode()))
    output_file.close()
    return decoded_message


def testeRLE():
    # the original string
    our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA"
    # pass in the original string
    encoded_message = encode_message(our_message)
    # pass in the decoded string
    decoded_message = decode_message(encoded_message)
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message + "]")
    print("Decoded string: [" + decoded_message + "]")
