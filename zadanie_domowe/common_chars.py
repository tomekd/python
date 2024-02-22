#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję common_chars(string1, string2), która zwraca alfabetycznie
uporządkowaną listę wspólnych liter z lańcuchów string1 i string2.
Oba napisy będą składać się wyłacznie z małych liter.
"""


def get_unique_chars(string_to_process):
    return set(''.join(string_to_process.split()))


def common_chars(string1, string2):
    return get_unique_chars(string1).intersection(get_unique_chars(string2))


input1 = "this is a string"
input2 = "ala ma kota"
output = ['a', 't']

print(common_chars(input1, input2))
