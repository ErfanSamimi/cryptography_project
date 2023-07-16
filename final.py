KEY_PERMUTATION_TABLE = [57, 49, 41, 33, 25, 17, 9,
                         1, 58, 50, 42, 34, 26, 18,
                         10, 2, 59, 51, 43, 35, 27,
                         19, 11, 3, 60, 52, 44, 36,
                         63, 55, 47, 39, 31, 23, 15,
                         7, 62, 54, 46, 38, 30, 22,
                         14, 6, 61, 53, 45, 37, 29,
                         21, 13, 5, 28, 20, 12, 4]

KEY_COMPRESSION_TABLE = [14, 17, 11, 24, 1, 5,
                         3, 28, 15, 6, 21, 10,
                         23, 19, 12, 4, 26, 8,
                         16, 7, 27, 20, 13, 2,
                         41, 52, 31, 37, 47, 55,
                         30, 40, 51, 45, 33, 48,
                         44, 49, 39, 56, 34, 53,
                         46, 42, 50, 36, 29, 32]

INIT_PERMUTATION_TABLE = [58, 50, 42, 34, 26, 18, 10, 1,
                          60, 52, 44, 36, 28, 20, 12, 4,
                          62, 54, 46, 38, 30, 22, 14, 6,
                          64, 56, 48, 40, 32, 24, 16, 8,
                          57, 49, 41, 33, 25, 17, 9, 2,
                          59, 51, 43, 35, 27, 19, 11, 3,
                          61, 53, 45, 37, 29, 21, 13, 5,
                          63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERMUTATION_TABLE = [8, 40, 48, 16, 56, 24, 64, 32,
                           39, 7, 47, 15, 55, 23, 63, 31,
                           38, 6, 46, 14, 54, 22, 62, 30,
                           37, 5, 45, 13, 53, 21, 61, 29,
                           36, 4, 44, 12, 52, 20, 60, 28,
                           35, 3, 43, 11, 51, 19, 59, 27,
                           34, 2, 42, 10, 50, 18, 58, 26,
                           33, 1, 41, 9, 49, 17, 57, 25]

EXPANSION_P_BOX_TABLE = [32, 1, 2, 3, 4, 5, 4, 5,
                         6, 7, 8, 9, 8, 9, 10, 11,
                         12, 13, 12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21, 20, 21,
                         22, 23, 24, 25, 24, 25, 26, 27,
                         28, 29, 28, 29, 30, 31, 32, 1]

S_BOXES = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

           [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

           [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

           [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

           [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

           [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

           [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

           [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]




def hex_to_bin(text):
    temp = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    output = ''
    for i in text:
        output += temp[i.upper()]

    return output


def dec_to_bin(data: str, output_length: int):
    return bin(int(data, 10))[2:].zfill(output_length)


def text_to_bin(text):
    text_hex = text.encode().hex()
    return hex_to_bin(text_hex)


def xor(string1: str, string2: str):
    assert len(string1) == len(string2)

    output = ""
    for i in range(len(string1)):
        assert string1[i] == '1' or string1[i] == '0'
        assert string2[i] == '1' or string2[i] == '0'

        output += str(int(string1[i]) ^ int(string2[i]))

    return output


def apply_permutation(text: str, permutation_table):
    output = ""
    for i in permutation_table:
        assert i >= 1
        output += text[i - 1]

    return output


def pad_text(text):
    padding_length = 8 - (len(text) % 8)
    padding = chr(padding_length) * padding_length
    return text + padding


def get_first_key(key_bin: str):
    assert len(key_bin) == 64

    key_56_bit = apply_permutation(key_bin, KEY_PERMUTATION_TABLE)

    assert len(key_56_bit) == 56

    left_key = key_56_bit[:28]
    right_key = key_56_bit[28:]

    new_key = left_key[1:] + left_key[0] + right_key[1:] + right_key[0]

    key_48_bit = apply_permutation(new_key, KEY_COMPRESSION_TABLE)
    assert len(key_48_bit) == 48

    return key_48_bit


def f_function(text_bin: str, key_48_bit, straight_pbox_table: list = None):


    assert len(text_bin) == 32, f"it's {len(text_bin)}"
    assert len(key_48_bit) == 48

    expanded_text = apply_permutation(text_bin, EXPANSION_P_BOX_TABLE)

    assert len(expanded_text) == 48

    xored_text = xor(expanded_text, key_48_bit)

    assert len(xored_text) == 48

    mixed_text = ""
    counter = 0
    for i in range(0, len(xored_text), 6):
        temp = xored_text[i: i + 6]
        column = int(temp[1:5], 2)
        row = int(temp[0] + temp[-1], 2)
        sbox = S_BOXES[counter]
        new_value = str(sbox[row][column])
        mixed_text += dec_to_bin(new_value, 4)
        counter += 1


    assert len(mixed_text) == 32

    if straight_pbox_table is None:
        pbox = [i for i in range(1, 33)]
    else:
        assert len(straight_pbox_table) == 32, f"it's {len(straight_pbox_table)}"
        pbox = straight_pbox_table

    return apply_permutation(mixed_text, pbox)


def get_after_and_before_pbox(plain_text: str, cipher_text_hex: str, key_hex: str):
    if len(plain_text) < 8:
        padded_plain = pad_text(plain_text)
    elif len(plain_text) == 8:
        padded_plain = plain_text
    else:
        raise ValueError(f"Invalid plain text length: {len(plain_text)}")

    temp_plain = text_to_bin(padded_plain)
    assert len(temp_plain) == 64
    plain_bin = apply_permutation(temp_plain, INIT_PERMUTATION_TABLE)
    assert len(plain_bin) == 64

    left_plain_bin = plain_bin[:32]
    right_plain_bin = plain_bin[32:]


    cipher_bin = apply_permutation(hex_to_bin(cipher_text_hex), INIT_PERMUTATION_TABLE)
    assert len(cipher_bin) == 64

    left_cipher_bin = cipher_bin[:32]
    right_cipher_bin = cipher_bin[32:]

    bin_key_64 = hex_to_bin(key_hex)
    first_key = get_first_key(key_bin=bin_key_64)

    # ========================================================================================================

    pbox_f_output = xor(left_cipher_bin, left_plain_bin)
    f_output = f_function(right_plain_bin, first_key)

    data = {
        'plain': plain_text,
        'b_pbox': pbox_f_output,
        'a_pbox': f_output,
        'x_pbox': xor(f_output, pbox_f_output)
    }

    return data

get_after_and_before_pbox(plain_text="Zendegi", cipher_text_hex="CF646E7170632D45", key_hex="4355262724562343")
def find_p_box():
    plain_and_Ciphers = {
        "kootahe": "6E2F7B25307C3144",
        "Zendegi": "CF646E7170632D45",
        "Edame": "D070257820560746",
        "Dare": "5574223505051150",
        "JolotYe": "DB2E393F61586144",
        "Daame": "D175257820560746",
        "DaemKe": "D135603D1A705746",
        "Mioftan": "D83C6F7321752A54",
        "Toosh": "413A2B666D024747",
        "HattaMo": "5974216034186B44",
        "khayeSa": "EA29302D74463545",
        "05753jj": "B1203330722B7A04",
        "==j95697": "38693B6824232D23",
        "\x08\x08\x08\x08\x08\x08\x08\x08": "1D1C0D0C4959590D",
    }

    pairs = list()

    for plain, cipher in plain_and_Ciphers.items():
        d = get_after_and_before_pbox(plain_text=plain, cipher_text_hex=cipher, key_hex="4355262724562343")
        pairs.append(d)

    data_list = list()

    for p in pairs:
        temp_data = {}
        before_pbox = p['b_pbox']
        after_pbox = p['a_pbox']
        for i in range(32):
            for j in range(32):
                if before_pbox[i] == after_pbox[j]:
                    if i in temp_data.keys():
                        temp_data[i].append(j)
                    else:
                        temp_data[i] = [j]

        data_list.append(temp_data)

    final_result = dict()

    for bit in range(32):
        intersection = [i for i in range(0, 32)]

        for data in data_list:
            intersection = [x for x in intersection if x in data[bit]]

        final_result[bit] = intersection

    output = []
    output_set = set()
    for k, v in final_result.items():
        s = v.pop()
        while s in output_set:
            s = v.pop()
        output.append(s)
        output_set.add(s)

    return output


def convert_to_text(binary: str):
    output = ''
    for i in range(0, len(binary), 8):
        output += chr(int(binary[i: i + 8], 2))
    return output


def decrypt(cipher_hex, table):
    cipher_bin = apply_permutation(hex_to_bin(cipher_hex), INIT_PERMUTATION_TABLE)
    assert len(cipher_bin) == 64

    left_cipher_binary = cipher_bin[:32]
    right_cipher_binary = cipher_bin[32:]

    d = f_function(
        right_cipher_binary,
        get_first_key(hex_to_bin('4355262724562343')),
        straight_pbox_table=[i + 1 for i in table]
    )
    assert len(d) == 32
    xored = xor(d, left_cipher_binary)

    temp = xored + right_cipher_binary

    assert len(temp) == 64
    plain_binary = apply_permutation(temp, FINAL_PERMUTATION_TABLE)

    return convert_to_text(plain_binary)


p_box = find_p_box()
print("Pbox is: ", p_box)
cipher = input()

plains = []

for i in range(0, len(cipher)-16, 16):
    plains.append(decrypt(cipher[i:i+16], p_box))

print(''.join(plains))
