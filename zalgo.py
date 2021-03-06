#!/usr/bin/env python3

import sys
import random
import argparse

def zalgo(text, intensity=(2, 5), top=False, middle=False, bottom=False):
    """Adds Unicode combining characters to each character in some text."""
    # All of these are the same right now; please categorize top, middle, and bottom marks.
    TOP_MARKS = [u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0304', u'\u0305', u'\u0306', u'\u0307', u'\u0308', u'\u0309', u'\u030a', u'\u030b', u'\u030c', u'\u030d', u'\u030e', u'\u030f', u'\u0310', u'\u0311', u'\u0312', u'\u0313', u'\u0314', u'\u0315', u'\u0316', u'\u0317', u'\u0318', u'\u0319', u'\u031a', u'\u031b', u'\u031c', u'\u031d', u'\u031e', u'\u031f', u'\u0320', u'\u0321', u'\u0322', u'\u0323', u'\u0324', u'\u0325', u'\u0326', u'\u0327', u'\u0328', u'\u0329', u'\u032a', u'\u032b', u'\u032c', u'\u032d', u'\u032e', u'\u032f', u'\u0330', u'\u0331', u'\u0332', u'\u0333', u'\u0334', u'\u0335', u'\u0336', u'\u0337', u'\u0338', u'\u0339', u'\u033a', u'\u033b', u'\u033c', u'\u033d', u'\u033e', u'\u033f', u'\u0340', u'\u0341', u'\u0342', u'\u0343', u'\u0344', u'\u0345', u'\u0346', u'\u0347', u'\u0348', u'\u0349', u'\u034a', u'\u034b', u'\u034c', u'\u034d', u'\u034e', u'\u034f', u'\u0350', u'\u0351', u'\u0352', u'\u0353', u'\u0354', u'\u0355', u'\u0356', u'\u0357', u'\u0358', u'\u0359', u'\u035a', u'\u035b', u'\u035c', u'\u035d', u'\u035e', u'\u035f', u'\u0360', u'\u0361', u'\u0362', u'\u0363', u'\u0364', u'\u0365', u'\u0366', u'\u0367', u'\u0368', u'\u0369', u'\u036a', u'\u036b', u'\u036c', u'\u036d', u'\u036e', u'\u036f']
    MIDDLE_MARKS = [u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0304', u'\u0305', u'\u0306', u'\u0307', u'\u0308', u'\u0309', u'\u030a', u'\u030b', u'\u030c', u'\u030d', u'\u030e', u'\u030f', u'\u0310', u'\u0311', u'\u0312', u'\u0313', u'\u0314', u'\u0315', u'\u0316', u'\u0317', u'\u0318', u'\u0319', u'\u031a', u'\u031b', u'\u031c', u'\u031d', u'\u031e', u'\u031f', u'\u0320', u'\u0321', u'\u0322', u'\u0323', u'\u0324', u'\u0325', u'\u0326', u'\u0327', u'\u0328', u'\u0329', u'\u032a', u'\u032b', u'\u032c', u'\u032d', u'\u032e', u'\u032f', u'\u0330', u'\u0331', u'\u0332', u'\u0333', u'\u0334', u'\u0335', u'\u0336', u'\u0337', u'\u0338', u'\u0339', u'\u033a', u'\u033b', u'\u033c', u'\u033d', u'\u033e', u'\u033f', u'\u0340', u'\u0341', u'\u0342', u'\u0343', u'\u0344', u'\u0345', u'\u0346', u'\u0347', u'\u0348', u'\u0349', u'\u034a', u'\u034b', u'\u034c', u'\u034d', u'\u034e', u'\u034f', u'\u0350', u'\u0351', u'\u0352', u'\u0353', u'\u0354', u'\u0355', u'\u0356', u'\u0357', u'\u0358', u'\u0359', u'\u035a', u'\u035b', u'\u035c', u'\u035d', u'\u035e', u'\u035f', u'\u0360', u'\u0361', u'\u0362', u'\u0363', u'\u0364', u'\u0365', u'\u0366', u'\u0367', u'\u0368', u'\u0369', u'\u036a', u'\u036b', u'\u036c', u'\u036d', u'\u036e', u'\u036f']
    BOTTOM_MARKS = [u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0304', u'\u0305', u'\u0306', u'\u0307', u'\u0308', u'\u0309', u'\u030a', u'\u030b', u'\u030c', u'\u030d', u'\u030e', u'\u030f', u'\u0310', u'\u0311', u'\u0312', u'\u0313', u'\u0314', u'\u0315', u'\u0316', u'\u0317', u'\u0318', u'\u0319', u'\u031a', u'\u031b', u'\u031c', u'\u031d', u'\u031e', u'\u031f', u'\u0320', u'\u0321', u'\u0322', u'\u0323', u'\u0324', u'\u0325', u'\u0326', u'\u0327', u'\u0328', u'\u0329', u'\u032a', u'\u032b', u'\u032c', u'\u032d', u'\u032e', u'\u032f', u'\u0330', u'\u0331', u'\u0332', u'\u0333', u'\u0334', u'\u0335', u'\u0336', u'\u0337', u'\u0338', u'\u0339', u'\u033a', u'\u033b', u'\u033c', u'\u033d', u'\u033e', u'\u033f', u'\u0340', u'\u0341', u'\u0342', u'\u0343', u'\u0344', u'\u0345', u'\u0346', u'\u0347', u'\u0348', u'\u0349', u'\u034a', u'\u034b', u'\u034c', u'\u034d', u'\u034e', u'\u034f', u'\u0350', u'\u0351', u'\u0352', u'\u0353', u'\u0354', u'\u0355', u'\u0356', u'\u0357', u'\u0358', u'\u0359', u'\u035a', u'\u035b', u'\u035c', u'\u035d', u'\u035e', u'\u035f', u'\u0360', u'\u0361', u'\u0362', u'\u0363', u'\u0364', u'\u0365', u'\u0366', u'\u0367', u'\u0368', u'\u0369', u'\u036a', u'\u036b', u'\u036c', u'\u036d', u'\u036e', u'\u036f']

    selected_marks = []
    if top:
        selected_marks += TOP_MARKS
    if middle:
        selected_marks += MIDDLE_MARKS
    if bottom:
        selected_marks += BOTTOM_MARKS
    selected_marks = list(set(selected_marks))

    if isinstance(intensity, int):
        intensity = (intensity, intensity + 1)

    output = []
    for char in text:
        output.append(char)
        if not char.isspace():
            mark_amount = random.randrange(intensity[0], intensity[1])
            for _ in range(mark_amount):
                mark = random.choice(selected_marks)
                output.append(mark)
    return ''.join(output)


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', help='input', required=True)
parser.add_argument('-p', '--power', dest='power', help='power', default=[2,5], type=int, nargs='+')  # One or two arguments only.
parser.add_argument('-t', '--top', dest='top', help='enables marks above text', action='store_true')
parser.add_argument('-m', '--middle', dest='middle', help='enables marks inside text', action='store_true')
parser.add_argument('-b', '--bottom', dest='bottom', help='enables marks under text', action='store_true')
args = parser.parse_args()

if len(args.power) == 1:
    args.power = args.power[0]
elif len(args.power) > 2:
    parser.error("argument -p/--power: expected 1 or 2 arguments")
    sys.exit()

output = zalgo(args.input, args.power, args.top, args.middle, args.bottom)
print(output)