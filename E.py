'''Даны две строки, состоящие из строчных латинских букв. Требуется определить,
являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.'''

from collections import Counter


def count(string):
    temp = list(string)
    collection = Counter()
    for word in temp:
        collection[word] += 1
    return collection


first = input()
second = input()

print(1 if count(first) == count(second) else 0)
