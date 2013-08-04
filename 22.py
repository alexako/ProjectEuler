#!/bin/python


def nameScore(name):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    scores = [(score, letter) for score, letter in enumerate(alphabet, start=1)]

    return sum([score[0] for letter in name for score in scores if letter in score])


def namePosition(name, nameList):
    return sum([place for place, n in enumerate(nameList, start=1) if name == n])

if __name__ == '__main__':
    f = open('names.txt')
    n = f.read().replace('"', '').split(',')
    names = [name for name in n if name]
    names.sort()

    print "Answer found: ", sum([namePosition(name, names) * nameScore(name) for name in names])
