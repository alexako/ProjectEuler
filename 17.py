ONES = {1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        0:' '
        }

TENS = {10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen'
        }

HIGHERS = {2:'twenty',
            3:'thirty',
            4:'forty',
            5:'fifty',
            6:'sixty',
            7:'seventy', 
            8:'eighty',
            9:'ninety',
            0:' ' 
            }


def transcribe(number):
    string = " "
    digits = [int(n) for n in str(number)]

    if len(digits) == 3:
        string += ONES[digits[0]]
        string += "hundred"
        if not (digits[1] == 0 and digits[2] == 0):
            string += "and"
        if digits[1] == 1:
            string += TENS[number % 100]
        else:
            string += HIGHERS[digits[1]]
            string += ONES[digits[2]]

    elif len(digits) == 2:
        if number in TENS:
            string += TENS[number]
        else:
            string += HIGHERS[digits[0]]
            string += ONES[digits[1]]

    elif len(digits) == 1:
            string += ONES[number]

    else:
        string = "onethousand"

    return string


def letter_count(string):
	return len(''.join(string.strip().split()))


if __name__ == '__main__':
    sum_of_letters = 0
    for i in xrange(1001):
        sum_of_letters += letter_count(transcribe(i))

    print "Answer found: ", sum_of_letters
