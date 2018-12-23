import sys
import math

def char2bin(char):
    char_ascii = ord(char)
    char_binaire = bin(char_ascii)[2:]
    #nb_zeros = 7 - len(char_binaire)
    #return nb_zeros * '0' + char_binaire
    #return char_binaire.zfill(7)
    return char_binaire.rjust(7, '0')


def text2bin(text):
    result = ''
    for letter in text:
        letter_bin = char2bin(letter)
        result += letter_bin
    return result


def bin2unaire(binaire):
    result = ''
    previous_bit = '2'
    length = 1
    for bit in binaire + '2':
        if bit == previous_bit:
            length += 1
        elif previous_bit != '2':
            if previous_bit == '0':
                result += '00 '
            else:
                result += '0 '
            result += '0' * length
            result += ' '
            length = 1
        previous_bit = bit
    return result


message = input()
message_bin = text2bin(message)
message_unaire = bin2unaire(message_bin)
#print(message_unaire)

print(message_unaire[:-1])