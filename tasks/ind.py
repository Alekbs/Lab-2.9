# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def brackets_check(s):
    if s:
        for char in s:
            if char.isalnum():
                s = s.replace(char, '')
        for bracket in brackets:
            s = s.replace(bracket, '')
        if s and all([bracket not in s for bracket in brackets]):
            return False

        return brackets_check(s)
    return True


if __name__ == '__main__':
    brackets = ['()', '[]']
    if brackets_check(input('Введите строку: ')):
        print('Скобки расставлены правильно.')
    else:
        print('Неправильная расстановка!')








