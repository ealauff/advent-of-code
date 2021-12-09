# --- Part Two ---
# Through a little deduction, you should now be able to determine the remaining digits.
# Consider again the first example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis,
# the mapping between signal wires and segments only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# So, the unique signal patterns would correspond to the following digits:

# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1
# Then, the four digits of the output value can be decoded:

# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3
# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example above,
# the output value of each entry can be determined:

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315
# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the four-digit output values.
# What do you get if you add up all of the output values?

# Your puzzle answer was XXXXXXX.

###########################################################################################################################################################################

import pathlib


def contains_segments(output_value, segments):
    difference = output_value ^ segments
    if len(difference) == len(output_value) - len(segments):
        return True
    return False


def find_decoder_segments(values_list):
    for value in values_list:
        num_segments = len(value)

        if num_segments == 3:
            decoder_1 = set(value)
        elif num_segments == 4:
            temp = set(value)

    decoder_2 = decoder_1 ^ temp
    return [decoder_1, decoder_2]


def decode_output(outputs_list, decoder_segments):
    decoded_output = ''
    decoder_1 = decoder_segments[0]
    decoder_2 = decoder_segments[1]

    for output in outputs_list:
        num_segments = len(output)

        if num_segments == 2:
            decoded_output += '1'

        elif num_segments == 3:
            decoded_output += '7'

        elif num_segments == 4:
            decoded_output += '4'

        elif num_segments == 7:
            decoded_output += '8'

        else:
            has_1 = contains_segments(set(output), decoder_1)
            has_2 = contains_segments(set(output), decoder_2)

            if num_segments == 5:
                if has_1:
                    decoded_output += '3'
                elif has_2:
                    decoded_output += '5'
                else:
                    decoded_output += '2'

            elif num_segments == 6:
                if has_1 and has_2:
                    decoded_output += '9'
                elif has_1:
                    decoded_output += '0'
                else:
                    decoded_output += '6'

    return int(decoded_output)


f = open(pathlib.Path(__file__).parent / 'input.txt', "r").read().splitlines()
sum_outputs = 0

for line in f:
    separate_values_outputs = line.split(' | ')
    values = separate_values_outputs[0].split()
    outputs = separate_values_outputs[1].split()

    decoder_segments = find_decoder_segments(values)
    sum_outputs += decode_output(outputs, decoder_segments)

print(sum_outputs)

# Use values to find the 2 sets of decoder segments
# From these 2 sets of segments (decoder_1 and decoder_2), all outputs can be decoded
# Repeat for each set of values and encoded outputs

# Decoder segments example:
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# decoder_1 = dab
#  dddd
#      a
#      a
#
#      b
#      b

# temp = eafb
#
# e    a
# e    a
#  ffff
#      b
#      b
#

# decoder_2 = def
#  dddd
# e
# e
#  ffff

# IMPROVEMENTS:
# FIRST CHECK OUTPUT TO SEE IF THERE ARE ANY UNIQUE NUMBERS IN THE OUTPUT
# ONLY VERIFY NON-UNIQUE NUMBERS IN THE OUTPUT
# DICT TO MAKE USE OF REPEATED DECODERS
# MAKE DECODE_OUTPUT NICER WITH ALL THOSE UGLY IF STATEMENTS

# Assumes that the 10 values given are the digits 0-9 in some random order
