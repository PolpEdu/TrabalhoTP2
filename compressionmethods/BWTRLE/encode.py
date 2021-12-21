

def bwt_tranf(d):
    Input = d
    assert "£" not in Input                     # Input string cannot contain $
    Input = Input + "£"                         # Add "$" to the end of the string

    table = [Input[i:] + Input[:i]
             for i in range(len(Input))]  # Table of rotations of string

    table = sorted(table)

    last_column = [row[-1:]
                   for row in table]             # Last characters of each row
    bwt = ''.join(last_column)
    return bwt


def rle_encode(data):
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
        return encoding


def decode(our_message):
    decoded_message = ""
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
    return decoded_message


BLOCKSIZE = 5000


def bwt_rle(write, texto):
    with open(write, "w") as f:
        f.close
    for i in range(0, len(texto), BLOCKSIZE):  # divisão em Blocos
        bwttry = bwt_tranf(texto[i-BLOCKSIZE:i])
        new_data = rle_encode(bwttry)
        with open(write, "a+") as f:
            for n in new_data:
                f.write(str(n))
