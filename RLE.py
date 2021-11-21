def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):

            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1

            else:
                break

        encoded_string = encoded_string + str(count) + ch
        i = j + 1

    #print("Encoded string: [" + encoded_string + "]")
    return encoded_string


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
