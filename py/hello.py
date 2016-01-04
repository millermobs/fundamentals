#!/usr/bin/env python3

import skilstak.colors as c
import time

def print_colored(word):
    """Makes each character a different color"""
    for char in word:
        print(c.rc() + char + c.x, end='')


def print_forever(message):
    """Print hello world to the console in random colors."""
    try:
        print(c.clear)
        while True: 
            #print(c.rc() + "Hello" + c.rc() + " " + who + "!", end="")
            print(c.rc() + message, end="")
    except KeyboardInterrupt:
        exit()

def print_colored(message):
    """Print hello world to the console with each word having a different color."""
    try:
        #print(c.random() + "Hello" + " " + c.random() + who + '!')
        print(c.multi(message))
    except KeyboardInterrupt:
        exit()

def print_boring(message):
    try:
        #print("Hello" + " " + who + "!")
        print(message)
    except KeyboardInterrupt:
        exit()

def parse_args():
    """Decides who to say hello to and the option/style it is written in"""
    import sys
    
    who = 'world'
    option = ''
    message = ''

    if len(sys.argv) > 2:
        option = sys.argv[1]
        who = sys.argv[2] 
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith('-'):
            option = sys.argv[1]
        else:
            who = sys.argv[1]
    return who, option
